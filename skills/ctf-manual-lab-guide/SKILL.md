---
name: ctf-manual-lab-guide
description: Teach an authorized CTF or training-lab technique as a hands-on step-by-step guide with exact tool launch, menu clicks, commands, expected observations, checkpoints, and troubleshooting. Use when the learner asks how to do a challenge manually or wants a guided practice lesson.
metadata:
  version: "1.0"
  provenance: "Locally authored at user request, 2026-09-11"
---

# CTF manual lab guide

Use this skill for learning, not for silently solving. Confirm that the target is a CTF, local binary, sandbox, or explicitly authorized training lab. If scope is unclear, pause before network interaction and ask for the lab scope.

## Teaching format

Create or update a Markdown lesson under:

`C:\Users\rapii\Documents\Skill-Library\02_CTF_Labs\manual-guides\<category>\`

Use a stable filename based on the challenge or topic. Structure every lesson as:

1. Objective and prerequisites.
2. Lab setup and exact workspace paths.
3. Tool map: what each tool is for and how to launch it.
4. Numbered actions. For GUI tools, name the window, menu, tab, button, field, and value to enter. For CLI tools, show the command and explain each important option.
5. Expected result after each meaningful action, including a small example shape rather than invented challenge values.
6. Checkpoint: what evidence confirms the learner can continue.
7. Manual reasoning: observation, hypothesis, test, conclusion.
8. Common mistakes and recovery steps.
9. Practice variation and a short self-check quiz.
10. Evidence and write-up notes.

Keep one learner action per step. Prefer copyable commands, but never fabricate a flag, token, endpoint, or output. Mark content as `Observed`, `Expected`, `Inferred`, or `To fill from the lab`. Explain destructive commands and keep them limited to the lab workspace.

## Tool guidance

Route to the smallest relevant existing skill: `ctf-toolkit` for local Python tooling, `source-reading-notes` for source code, `ctf-memory` for reusable lessons, and `ctf-writeup-builder` after the learner confirms the solve. Use Ghidra/Burp/GDB instructions only when the relevant artifact and authorized lab scope are present. Do not load every skill or every write-up.

## Interaction mode

When working interactively, teach one phase at a time and wait for the learner's result before advancing. If the learner asks for a full printable guide, write the complete Markdown file. If the learner asks for a hint, reveal only the next checkpoint, not the full solution. If they say stuck or rabbit hole, summarize evidence and the next two bounded tests.

## Karpathy-style operating rules

Apply these compact rules in every lesson:

- Think before acting: state the current assumption and name what evidence would disprove it.
- Simplicity first: use the smallest safe test that distinguishes the likely hypotheses; do not spray payloads or load unrelated skills.
- Surgical changes: preserve the learner's session and artifacts; change only the request field or lab input required by the current test.
- Goal-driven execution: define a checkpoint before each phase and stop when it is met, contradicted, or needs user input.

Use this mini-loop in the guide:

`Where → Why → How → Expected evidence → Actual evidence → Next/Stop`

If evidence conflicts, do not silently pick a story. Report the conflict, revert to the last known checkpoint, and propose at most two bounded next tests.

## Safety and quality

Do not scan unrelated systems, contact live targets, bypass authorization, steal credentials, or provide stealth/evasion guidance. Redact secrets and live credentials from saved lessons. Keep commands reproducible and scoped. At the end, offer to convert the completed lesson into a formal write-up and add only one compact, non-secret lesson to CTF memory.
