---
name: burp-mcp-bridge
description: Use the configured PortSwigger Burp MCP bridge for authorized CTF or training-lab HTTP testing, history review, Repeater, and response comparison.
metadata:
  version: "1.0"
  provenance: "Locally authored 2026-09-11"
---

# Burp MCP bridge

Use only for authorized CTF/training labs and only when the `burp` MCP server
is connected. A Skill cannot create Burp connectivity. If unavailable, report
the limitation and use only an explicitly permitted fallback.

At task start confirm Burp is running, the PortSwigger extension is loaded, MCP
is enabled on `127.0.0.1:9876`, and the target is allowlisted. Use the loop:
`Where → Why → How → Expected evidence → Actual evidence → Next/Stop`.
Continue until a verified flag/success condition or genuine blocker. After
three materially equivalent failures, run `rabbit-hole-check`, revise the
assumption, and allow at most two evidence-driven tests. Redact secrets.
