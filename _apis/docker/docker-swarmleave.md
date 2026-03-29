---
aid: docker:docker-swarmleave
name: Swarm Leave
tags:
- Swarm
- Leave
humanURL: 
properties: []
description: >-
  The Docker Swarm Leave POST operation allows a node to leave an existing Docker Swarm cluster. When executed, this endpoint removes the node from the swarm, effectively disconnecting it from the cluster's shared resources and workload distribution. The operation typically requires a force parameter to be set to true if the node is a manager, as managers need explicit confirmation to leave the swarm to prevent accidental disruption of cluster management. Once a node leaves the swarm, it return...

---
