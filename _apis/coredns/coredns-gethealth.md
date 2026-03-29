---
aid: coredns:coredns-gethealth
name: CoreDNS liveness health check
tags:
- Health
humanURL: 
properties: []
description: >-
  Returns the overall health status of the CoreDNS process. Returns HTTP 200 with body "OK" when CoreDNS is alive and healthy. Returns HTTP 503 during the lameduck shutdown period to signal that the instance is draining and should not receive new traffic. This endpoint is typically used as the Kubernetes liveness probe target.

---
