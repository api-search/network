---
aid: etcd:etcd-clustermemberremove
name: Remove a member from the cluster
tags:
- Cluster
humanURL: 
properties: []
description: >-
  Removes an existing member from the etcd cluster identified by its member ID. The removed member is immediately excluded from the cluster's Raft quorum. Removing a member that holds the leadership will trigger a new leader election. Care must be taken to maintain quorum when removing members from small clusters.

---
