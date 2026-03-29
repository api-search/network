---
aid: etcd:etcd-maintenancetransferleadership
name: Transfer cluster leadership
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Transfers the Raft leadership from the current leader to the specified target member. This operation is useful during maintenance to gracefully move leadership away from a member that needs to be taken offline. The target member must be a healthy voting member of the cluster for the transfer to succeed.

---
