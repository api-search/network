---
aid: docker:docker-nodeupdate
name: Node Update
tags:
- Node
- Update
humanURL: 
properties: []
description: >-
  This API operation updates the configuration of a specific node in a Docker Swarm cluster by sending a POST request to the /nodes/{id}/update endpoint, where {id} represents the unique identifier of the target node. It allows administrators to modify node attributes such as availability (active, pause, or drain), role (worker or manager), labels, and other node-specific settings. The operation typically requires the node's current version number to ensure safe concurrent updates and prevent c...

---
