---
aid: docker:docker-networkdelete
name: Network Delete
tags:
- Network
- Delete
humanURL: 
properties: []
description: >-
  This API operation removes a specified Docker network from the system by sending a DELETE request to the `/networks/{id}` endpoint, where `{id}` is the unique identifier of the network to be deleted. When executed, it permanently deletes the network configuration and removes it from Docker's network management system, freeing up resources and making the network name available for reuse. The operation will fail if containers are still attached to the network, requiring those containers to be d...

---
