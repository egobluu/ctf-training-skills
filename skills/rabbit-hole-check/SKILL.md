---
name: rabbit-hole-check
description: Pause repetitive reasoning and summarize evidence when the user says rabbit hole, stuck, or going in circles. Supports study, debugging, and retrospective CTF notes without selecting or executing attack techniques.
metadata:
  version: "1.0"
  provenance: "Locally authored at user request, 2026-09-11"
---

# Rabbit-hole check

Help the user recognize unproductive repetition using existing conversation evidence. This is a reflection checkpoint, not a planner or executor. Do not call tools, dispatch agents, select attack skills, generate payload variants, or propose exploitation pivots through this skill.

## When to pause

Offer one brief checkpoint after three materially equivalent unsuccessful attempts with no new information, or immediately when requested. Count the underlying assumption, not superficial wording or parameter changes. One failure is insufficient. If earlier attempts are unavailable, say the history is incomplete instead of inventing a count.

A user-specified time or attempt budget overrides this default. Do not claim elapsed time without timestamps. A long computation that is still producing useful results is not necessarily a rabbit hole.

## Checkpoint

Use at most six short lines in the user's language:

- Goal: the original question or desired result.
- Observed: up to three facts with pointers to existing messages, files, or output already available.
- Assumed: the main unverified assumption; keep it separate from facts.
- Repetition: what was repeated and whether it added evidence.
- Uncertainty: what the available evidence cannot establish.
- Pause decision: summarize notes, take a break, request a conceptual hint, or return to the original problem statement.

Do not treat failure as proof that an assumption is false. Distinguish contradictory evidence, missing prerequisites, inconclusive output, and unavailable information. Never invent findings or flags.

After the checkpoint, stop the repetition. Do not silently switch to another operational approach. A request to continue is not itself new evidence. If asked to summarize again with unchanged evidence, refer to the prior checkpoint briefly instead of repeating a lengthy analysis.

## Keep overhead small

Maintain only a compact mental note of the assumption, last observation, and repetition count. Use current context; do not scan skill libraries or create logs unless separately requested. Do not interrupt each tool call or emit recurring warnings. This skill sets no background timer and cannot guarantee automatic interception of another agent's actions.
