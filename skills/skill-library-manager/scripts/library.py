"""Read-only skill inventory. Discovered scripts and instructions are never executed."""
import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path

REPARSE = 0x400
OFFLINE = 0x1000
RECALL = 0x40000 | 0x400000


def write_report(out, name, data):
    out.mkdir(parents=True, exist_ok=True)
    (out / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def scan(roots, out):
    found, skipped, aliases = [], [], []
    visited = set()
    pending = list(roots)
    last = time.monotonic()
    while pending:
        directory = os.path.abspath(pending.pop())
        try:
            attributes = getattr(os.lstat(directory), "st_file_attributes", 0)
            if os.path.islink(directory) or attributes & (REPARSE | OFFLINE | RECALL):
                skipped.append({"path": directory, "reason": "root link/reparse/offline"})
                if os.path.islink(directory) or (hasattr(os.path, "isjunction") and os.path.isjunction(directory)):
                    aliases.append({"source": directory, "target": os.path.realpath(directory), "type": "filesystem-alias"})
                continue
        except OSError as error:
            skipped.append({"path": directory, "reason": type(error).__name__})
            continue
        key = os.path.normcase(directory)
        if key in visited:
            continue
        visited.add(key)
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    try:
                        stat = entry.stat(follow_symlinks=False)
                        attributes = getattr(stat, "st_file_attributes", 0)
                        if entry.is_symlink() or attributes & REPARSE:
                            skipped.append({"path": entry.path, "reason": "link or reparse point"})
                            if entry.is_symlink() or (hasattr(os.path, "isjunction") and os.path.isjunction(entry.path)):
                                aliases.append({"source": entry.path, "target": os.path.realpath(entry.path), "type": "filesystem-alias"})
                            continue
                        if entry.is_dir(follow_symlinks=False):
                            pending.append(entry.path)
                        elif entry.name.lower() == "skill.md":
                            if attributes & (OFFLINE | RECALL):
                                skipped.append({"path": entry.path, "reason": "cloud/offline placeholder"})
                                continue
                            if stat.st_size > 2_000_000:
                                skipped.append({"path": entry.path, "reason": "oversized skill entrypoint"})
                                continue
                            raw = Path(entry.path).read_bytes()
                            content = raw.decode("utf-8-sig", errors="replace")
                            front = re.match(r"\A---\s*\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
                            name = re.search(r"(?m)^name:\s*(.+)$", front.group(1)) if front else None
                            found.append({"path": entry.path, "name": name.group(1).strip().strip('\"\'') if name else None, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "frontmatter_present": bool(front), "has_scripts": (Path(entry.path).parent / "scripts").is_dir()})
                    except OSError as error:
                        skipped.append({"path": entry.path, "reason": type(error).__name__})
        except OSError as error:
            skipped.append({"path": directory, "reason": type(error).__name__})
        if time.monotonic() - last > 20:
            print(json.dumps({"directories": len(visited), "skills": len(found)}), flush=True)
            last = time.monotonic()
    found.sort(key=lambda item: item["path"].lower())
    hashes, names = {}, {}
    for item in found:
        hashes.setdefault(item["sha256"], []).append(item["path"])
        if item["name"]:
            names.setdefault(item["name"], []).append(item["path"])
    duplicates = [{"sha256": key, "paths": values} for key, values in hashes.items() if len(values) > 1]
    edges = list(aliases)
    for group in duplicates:
        edges.extend({"source": group["paths"][0], "target": path, "type": "same-entrypoint-hash"} for path in group["paths"][1:])
    summary = {"roots": roots, "directories_scanned": len(visited), "skill_files": len(found), "duplicate_entrypoint_groups": len(duplicates), "duplicate_name_groups": sum(len(v) > 1 for v in names.values()), "skipped": len(skipped), "note": "Matching SKILL.md files do not prove entire skill folders are interchangeable."}
    for filename, data in [("catalog.json", found), ("duplicates.json", duplicates), ("names.json", {k:v for k,v in names.items() if len(v)>1}), ("graph.json", edges), ("skipped.json", skipped), ("summary.json", summary)]:
        write_report(out, filename, data)
    print(json.dumps(summary), flush=True)


def check(roots, out):
    entries = []
    for root in roots:
        try:
            for path in Path(root).iterdir():
                linked = path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())
                entries.append({"path": str(path), "linked": linked, "target": os.path.realpath(path) if linked else None, "skill_present": (path / "SKILL.md").is_file(), "broken_link": linked and not path.exists()})
        except OSError as error:
            entries.append({"path": root, "error": type(error).__name__})
    write_report(out, "discovery.json", entries)
    print(json.dumps({"entries": len(entries), "broken_links": sum(e.get("broken_link", False) for e in entries)}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["scan", "check"])
    parser.add_argument("--root", action="append", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    (scan if args.command == "scan" else check)(args.root, args.out)


if __name__ == "__main__":
    main()
