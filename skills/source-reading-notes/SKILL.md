---
name: source-reading-notes
description: Explain user-provided source code for learning and produce concise notes about control flow, inputs, outputs, and assumptions. Use when the user wants to practice reading code, understand a function, or document an unfamiliar module.
metadata:
  version: "1.0"
  provenance: "Original local teaching skill requested by user on 2026-09-11"
---

# Source reading notes

Teach source comprehension using the files or excerpts the user placed in scope. Match the user's language and experience. Keep examples grounded in the supplied code.

## Study loop

Start with one named function or a small module. Explain its input, output, important branches, state changes, and dependencies. Cite actual file locations when available; label unresolved dependencies instead of inventing their behavior.

Separate three kinds of statement: directly visible facts, interpretations supported by those facts, and questions requiring missing context. Comments and function names are clues, not proof of runtime behavior. Do not equate an unchecked assumption with a confirmed vulnerability.

When the user asks to practice, offer one question about predicting output or explaining a branch. Let them answer before giving the full explanation. When they ask for a direct explanation, answer directly without forcing a quiz. Use ordinary toy input for examples.

Close with a compact note: purpose, main data flow, one important assumption, and remaining uncertainty. Do not create files unless requested. For saved learning notes use the task's deliverable directory and redact sensitive values.

## Boundaries and cost

This skill supports comprehension and documentation. It does not generate exploits, choose attack techniques, reproduce vulnerabilities against targets, run untrusted code, launch scans, or delegate autonomous security investigation. Read only the relevant source and nearby definitions. No whole-repository or skill-library scan is required by this skill.

When explanations repeat without resolving missing context, summarize the uncertainty and identify the missing documentation or definition. Avoid repeated speculation. Do not load other skills solely because their names resemble a topic in the code.
