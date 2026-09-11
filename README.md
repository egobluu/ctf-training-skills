# CTF Training Skills

A curated, scoped skill library for authorized CTFs, security training labs, and pentest practice.

## What is included

- CTF workflow: manual guided practice, toolkit routing, memory, write-ups, flag reporting, and auto-enrichment.
- Web/API testing: recon, authentication, authorization/BOLA, injection, SSRF, SSTI, XSS, XXE, race conditions, JWT/OAuth, request smuggling, WebSockets, and business logic.
- Binary, crypto, forensics, Linux/Windows privilege escalation, containers, Kubernetes, and pivoting.
- Safety and organization: scoped testing, evidence-first notes, rabbit-hole checks, and skill-library management.

## Operating loop

`Where → Why → How → Expected evidence → Actual evidence → Next/Stop`

Use the smallest relevant skill. Work only on CTFs, local labs, or explicitly authorized targets. Do not scan unrelated systems, expose credentials, or run untrusted repository code.

## Automatic documentation

After a confirmed solve, use `ctf-writeup-builder` to create a reproducible write-up and `ctf-memory` to record one compact, non-secret lesson. `ctf-manual-lab-guide` teaches the same process step by step with GUI locations, commands, checkpoints, and troubleshooting.

## Notes

This repository is a curated export for learning. Review each skill and its provenance before deploying it in another agent environment. The canonical local library remains the source of truth for the user's configured agents.

## Extended practice pack

The `skills/extended/ljagiello-ctf-skills/` directory adds category-level practice material for pwn, reverse engineering (including Android/native RE topics), crypto, forensics, malware, misc, OSINT, AI/ML, and write-ups. It is kept under an extended namespace to avoid routing collisions and context bloat.

Source reviewed: `https://github.com/ljagiello/ctf-skills` at commit `36c72e53a96a035791821caff7440882ea0f5c57`.

The `verialabs/ctf-agent` runtime was reviewed but intentionally not copied: it is an autonomous multi-model CTFd solver that requires provider keys, Docker, and external CTFd access. We retained its high-level ideas as reference only, not as an automatic execution loop.
