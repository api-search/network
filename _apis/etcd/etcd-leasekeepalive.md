---
aid: etcd:etcd-leasekeepalive
name: Renew a lease
tags:
- Lease
humanURL: 
properties: []
description: >-
  Renews an existing lease to prevent it from expiring. Clients must call this endpoint periodically with an interval shorter than the lease TTL to maintain the lease. The response returns the remaining TTL of the lease after the renewal. If the lease has already expired, an error is returned and a new lease must be granted.

---
