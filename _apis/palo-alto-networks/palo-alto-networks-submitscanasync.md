---
aid: palo-alto-networks:palo-alto-networks-submitscanasync
name: Palo Alto Networks Submit an asynchronous AI security scan
tags:
- Scan
humanURL: 
properties: []
description: >-
  Submits one or more prompt/response pairs for asynchronous security analysis. Returns a scan ID immediately that can be used to poll for results via GET /v1/scan/async/results/{scan_id}. Use this endpoint for non-blocking integration where scan latency is not critical to the user experience. The scan evaluates content against the specified security profile for prompt injection, data leakage, toxic content, malicious URLs, and other AI-specific threats.

---
