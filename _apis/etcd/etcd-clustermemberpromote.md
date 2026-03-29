---
aid: etcd:etcd-clustermemberpromote
name: Promote a learner member
tags:
- Cluster
humanURL: 
properties: []
description: >-
  Promotes a learner (non-voting) member to a full voting member of the etcd cluster. The learner must be caught up with the cluster's Raft log before it can be promoted. This two-phase approach (add as learner, then promote) provides a safer way to grow clusters without temporarily reducing quorum availability.

---
