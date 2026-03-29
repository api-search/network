---
aid: coredns:coredns-getreadiness
name: CoreDNS readiness check
tags:
- Ready
humanURL: 
properties: []
description: >-
  Returns the readiness status of all CoreDNS plugins. Returns HTTP 200 with body "OK" when all plugins that implement the Readiness interface report they are ready to serve traffic. Returns HTTP 503 if any plugin is not yet ready. This endpoint is typically used as the Kubernetes readiness probe target and requires the ready plugin to be enabled in the Corefile.

---
