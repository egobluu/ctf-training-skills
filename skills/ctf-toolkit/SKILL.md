---
name: ctf-toolkit
description: Use the shared local CTF Python environment for authorized lab challenges. Select only the relevant tool for the provided artifact and keep results concise.
metadata:
  version: "1.0"
  provenance: "Locally configured 2026-09-11"
---

# CTF toolkit

The shared environment is `C:\Users\rapii\Documents\Skill-Library\02_CTF_Labs\tools\ctf-python\.venv`. Use its Python or console scripts when the required package is installed. It contains pwntools, z3-solver, scapy, volatility3, pycryptodome, requests, BeautifulSoup, and lxml.

Choose based on the artifact: pwntools for local CTF binaries and challenge services, Z3 for constraints, Scapy for packets, Volatility 3 for memory images, PyCryptodome for cryptographic transformations, and requests/BeautifulSoup for HTTP material in scope. Prefer read-only parsing and local challenge files. Do not scan unrelated systems or run payloads against targets without explicit scope.

Keep outputs bounded: inspect metadata and a small relevant slice first, then expand only when evidence requires it. Record commands and hashes for reproducibility. Never expose tokens, private keys, or challenge credentials in notes.

Existing system tools include GDB, ROPgadget, checksec, Java, and Ghidra/Ghidra MCP. This skill does not start daemons, configure Burp, or invoke arbitrary code from untrusted repositories.
