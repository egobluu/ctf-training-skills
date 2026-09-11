# Scammer's

Platform: not independently established in the reviewed source; its frontmatter uses the label "01 CTF Archives".

Category: OSINT / repository-history exposure, as described by the local writeup.

Evidence status: local writeup reports finding sensitive data in historical repository content. No live repository or platform acceptance was checked in this task.

Observation: the writeup reports that removing a sensitive file from the current repository tree did not remove its historical contents.

Lesson: treat a committed secret as exposed. Remediation includes revocation or rotation, reviewing its use, preventing recurrence through secret scanning and appropriate storage, and assessing history cleanup separately. Removing the current file alone is insufficient.

Source: `C:\Users\rapii\Documents\Codex\2026-08-01\1-scammer-s-100-0-0\outputs\writeup-1-scammers.md`. The companion provenance.json records the hash at review time. No secret value, target endpoint, or retrieval procedure is included.
