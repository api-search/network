---
aid: etcd:etcd-maintenancestatus
name: Get member status
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Returns the status of the etcd member that receives the request, including the cluster ID, member ID, Raft index, Raft term, Raft applied index, and whether the member is a learner. The leader field contains the member ID of the current cluster leader. This endpoint is useful for monitoring the health and state of individual cluster members.

---
