---
aid: docker:docker-nodedelete
name: Node Delete
tags:
- Node
- Delete
humanURL: 
properties: []
description: >-
  Removes a specified node from the Docker Swarm cluster by its unique identifier. This operation is typically used when decommissioning a node or removing a failed node from the swarm. The node must be in a down state or demoted from manager status before deletion, and any tasks running on the node should be drained or rescheduled to other nodes first. Once deleted, the node's data is permanently removed from the swarm's internal state, and the node would need to be rejoined to the cluster if ...

---
