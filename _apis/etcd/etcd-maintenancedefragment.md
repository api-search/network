---
aid: etcd:etcd-maintenancedefragment
name: Defragment a member's backend
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Defragments the storage backend of the etcd member that receives the request, reclaiming disk space from deleted keys. Defragmentation is an expensive operation that blocks the member from serving requests during the process. It should be performed during maintenance windows on individual members rather than on all cluster members simultaneously.

---
