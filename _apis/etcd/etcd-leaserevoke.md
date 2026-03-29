---
aid: etcd:etcd-leaserevoke
name: Revoke a lease
tags:
- Lease
humanURL: 
properties: []
description: >-
  Revokes an existing lease identified by its lease ID. When a lease is revoked, all keys attached to that lease are automatically deleted from the etcd cluster. This is useful for releasing distributed locks or invalidating all session-scoped keys at once.

---
