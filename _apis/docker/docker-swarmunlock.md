---
aid: docker:docker-swarmunlock
name: Swarm Unlock
tags:
- Swarm
- Unlock
humanURL: 
properties: []
description: >-
  ``` The Docker Swarm Unlock POST operation is used to unlock a locked swarm manager by providing the unlock key. When a swarm is configured with autolock enabled, manager nodes require an unlock key to decrypt their Raft logs after a restart, preventing unauthorized access to sensitive swarm data. This endpoint accepts the unlock key in the request body and attempts to unlock the swarm manager, allowing it to rejoin the swarm cluster and resume normal operations. If the provided unlock key is...

---
