---
aid: cockroachdb:cockroachdb-health
name: Check node health
tags:
- Health
humanURL: 
properties: []
description: >-
  Reports the health of the CockroachDB node. When the optional ready parameter is set to true, the endpoint also verifies that the node is fully operational and ready to accept SQL connections. Returns HTTP 200 if healthy, or HTTP 500 if not ready. This endpoint does not require authentication.

---
