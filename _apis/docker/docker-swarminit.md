---
aid: docker:docker-swarminit
name: Swarm Init
tags:
- Swarm
humanURL: 
properties: []
description: >-
  Initialize a new swarm cluster by configuring the Docker engine to operate in swarm mode, making the current node the first manager node of the swarm. This operation sets up the Raft consensus protocol for cluster management, generates join tokens for adding worker and manager nodes, and configures the swarm's network settings including the advertised address, listen address, and data path address. The endpoint accepts configuration parameters such as specifications for the Certificate Author...

---
