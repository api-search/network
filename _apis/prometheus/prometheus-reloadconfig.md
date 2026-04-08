---
aid: prometheus:prometheus-reloadconfig
name: Prometheus Reload configuration
tags:
- Lifecycle
humanURL: 
properties: []
description: >-
  Triggers a reload of the Prometheus configuration file and rule files. Returns 200 when the reload is successful and 500 if the reload fails. Requires --web.enable-lifecycle flag. Also triggered by sending SIGHUP to the Prometheus process.

---
