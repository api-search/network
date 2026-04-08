---
aid: spire:spire-getliveness
name: SPIRE Liveness probe
tags:
- Health
humanURL: 
properties: []
description: >-
  Returns HTTP 200 if the SPIRE component process is alive and running. A non-200 response or connection failure indicates the process should be restarted. This endpoint is suitable for use as a Kubernetes livenessProbe. The path can be customized via the live_path configuration option (default: /live).

---
