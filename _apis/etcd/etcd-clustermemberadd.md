---
aid: etcd:etcd-clustermemberadd
name: Add a member to the cluster
tags:
- Cluster
humanURL: 
properties: []
description: >-
  Adds a new member to the etcd cluster. The peer URLs of the new member must be provided. The new member starts in an unstarted state and is considered a learner until it catches up with the cluster's Raft log. The isLearner field can be set to true to explicitly add the member as a non-voting learner member.

---
