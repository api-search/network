---
aid: traefik:traefik-ping
name: Traefik Health check ping
tags:
- Health
humanURL: 
properties: []
description: >-
  Returns HTTP 200 with body "OK" when the Traefik process is alive and ready. Used for liveness probes in container orchestration. Note that the ping endpoint is typically configured on a separate entry point or path outside the /api prefix.

---
