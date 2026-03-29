---
aid: etcd:etcd-maintenancesnapshot
name: Stream a database snapshot
tags:
- Maintenance
humanURL: 
properties: []
description: >-
  Streams a point-in-time snapshot of the etcd database as a binary blob. The snapshot can be used to create a backup of the etcd data or to restore a cluster to a previous state. The snapshot is streamed in chunks to support large database sizes. This operation should be performed on a healthy cluster member to ensure consistency.

---
