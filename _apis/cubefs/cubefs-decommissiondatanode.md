---
aid: cubefs:cubefs-decommissiondatanode
name: Decommission a data node
tags:
- DataNodes
humanURL: 
properties: []
description: >-
  Removes a data node from the cluster. All data partitions on the node are asynchronously migrated to other available data nodes before the node is fully removed. This is a safe operation for draining a node during maintenance or replacement.

---
