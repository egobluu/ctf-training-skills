---
name: ctf-writeup-builder
description: Automatically turn a completed CTF session into a concise reproducible write-up using only verified evidence from the session. Use when a challenge is solved or the user requests a write-up.
metadata:
  version: "1.0"
  provenance: "Locally authored at user request, 2026-09-11"
---

# CTF write-up builder

When a CTF flag or final answer is confirmed, create a Markdown write-up in `C:\Users\rapii\Documents\Skill-Library\02_CTF_Labs\writeups\<category>\`. Use a stable filename derived from the known challenge name; if identity is unclear use `unknown-<date>`. Keep the challenge's original artifacts in its workspace.

Use this order: challenge and category, goal, provided artifacts, observations, hypotheses, verification steps, dead ends and why they were dropped, solution explanation, evidence and exact result, lessons learned, and defensive takeaway. Mark each statement as observed, inferred, or unverified when that distinction matters. Include commands only when they are safe, necessary to reproduce a local or explicitly scoped lab result, and already present in the session evidence.

Before writing, check whether the same challenge write-up exists. Update it only when new verified evidence improves it; otherwise leave it unchanged. Never invent flags, normalize exact values, claim platform acceptance without evidence, or copy credentials and private tokens into the write-up. Redact live endpoints and secrets unless the user explicitly asks for a private local record.

At the end, invoke `ctf-memory` conceptually by extracting one compact lesson and adding it to the memory index. Do not reread all write-ups. If the user asks for only the flag, use `ctf-flag-reporter` and do not create a long write-up unless requested.

This skill produces documentation. It does not solve a challenge, run a scanner, contact a target, or select an attack path.
