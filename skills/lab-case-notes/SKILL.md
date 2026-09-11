---
name: lab-case-notes
description: Turn existing CTF or training-lab writeups into evidence-linked case notes and defensive lessons, grouping related cases without creating a separate skill for every challenge.
---

# Lab case notes

Maintain one small skill and append case data instead of making one discoverable skill per challenge. Read only the case relevant to the requested retrospective.

Before calling a case solved, distinguish an author's reported result, a locally verified artifact, and an accepted submission. A flag printed in a writeup does not establish platform acceptance. Record the source path and its hash, and mark missing evidence explicitly. Do not rerun a solve or contact a target merely to fill a missing field.

For each case, record its title, platform if established, category, evidence status, high-level observation, defensive or analytical lesson, and source reference. Keep challenge inputs, credentials, target endpoints, payloads, and executable exploit recipes out of these reusable notes. Preserve the original evidence separately; never delete it because a summary exists.

Group cases by the mechanism or lesson. Name/description similarity is a search aid, not proof that workflows or skill packages can replace each other. Reuse an existing lesson when appropriate and keep distinct evidence for each case.

Existing cases:

- [ORBITAL DOCKING HANDSHAKE](references/orbital-docking.md): a local writeup's static-analysis findings and the limits of obfuscation.
- [Scammer's](references/scammers.md): a local writeup's reported exposure of sensitive data in repository history and the importance of rotation.

This skill produces documentation only. It does not build attack agents, execute archived procedures, or infer permission to test another system.
