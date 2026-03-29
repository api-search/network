---
aid: etcd:etcd-maintenancehash
name: Get member backend hash
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Returns a hash of the etcd member's backend database. This hash can be used to verify data consistency across cluster members. If members report different hashes, it may indicate a data corruption issue. This endpoint is primarily used for debugging and consistency verification.

---
