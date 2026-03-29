---
aid: etcd:etcd-kvtxn
name: Execute a transaction
tags:
- KV
humanURL: 
properties: []
description: >-
  Executes an atomic compare-and-swap transaction against the etcd key-value store. A transaction consists of a set of compare conditions, a success branch of operations executed if all conditions are true, and a failure branch executed if any condition is false. Transactions are atomic and isolated, providing strong consistency guarantees within the etcd cluster.

---
