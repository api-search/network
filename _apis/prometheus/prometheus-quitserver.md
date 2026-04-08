---
aid: prometheus:prometheus-quitserver
name: Prometheus Graceful shutdown
tags:
- Lifecycle
humanURL: 
properties: []
description: >-
  Triggers a graceful shutdown of the Prometheus server. Returns 200 immediately while the shutdown proceeds asynchronously. Requires --web.enable-lifecycle flag. Also triggered by sending SIGTERM to the Prometheus process.

---
