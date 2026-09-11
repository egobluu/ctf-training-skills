---
name: ctf-memory
description: Maintain a compact searchable memory of lessons from completed CTF challenges. Use automatically at CTF start and after a confirmed solve to reuse patterns without loading all past writeups.
metadata:
  version: "1.0"
  provenance: "Locally authored at user request, 2026-09-11"
---

# CTF memory

Keep the canonical index in `C:\Users\rapii\Documents\Skill-Library\02_CTF_Labs\memory\INDEX.md` and one short note per confirmed challenge in the same directory under `cases\`. Read only the category or tag relevant to the current challenge. Do not load the full memory directory by default.

At CTF start, identify category, artifact type, and two or three relevant tags; read matching memory notes if they exist. Do not treat a memory note as proof that the same technique applies. Revalidate against current evidence.

After a flag or final answer is confirmed, append or update one note containing challenge identity, category, evidence status, high-level mechanism, failed assumption, successful observation, reusable defensive lesson, and tags. Keep flags, tokens, passwords, private keys, target credentials, live endpoints, and executable exploit recipes out of reusable memory. Put exact sensitive evidence only in the challenge workspace.

Use `unknown` when identity or evidence status is unavailable. Never invent a result. If no new lesson was learned, do not create a duplicate note. Keep each note under 300 words and update the index with a one-line search entry.

This skill is documentation and retrieval only. It does not scan targets, execute payloads, or infer authorization.
