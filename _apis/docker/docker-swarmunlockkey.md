---
aid: docker:docker-swarmunlockkey
name: Swarm Unlockkey
tags:
- Swarm
humanURL: 
properties: []
description: >-
  The Docker Swarm Unlockkey GET operation retrieves the unlock key required to access a locked Docker Swarm manager node after it has been restarted. When a Swarm cluster is configured with autolock enabled for enhanced security, manager nodes encrypt their Raft logs at rest and require an unlock key to decrypt them upon restart. This endpoint returns the current unlock key that administrators need to manually unlock manager nodes using the docker swarm unlock command, ensuring that sensitive ...

---
