---
aid: docker:docker-networkdisconnect
name: Network Disconnect
tags:
- Network
- Disconnect
humanURL: 
properties: []
description: >-
  Disconnects a container from a specified Docker network by sending a POST request to the /networks/{id}/disconnect endpoint, where {id} is the network identifier. This operation removes the network attachment from a running or stopped container, effectively isolating it from that particular network while potentially maintaining connections to other networks. The request body typically includes the container ID or name to be disconnected, and optionally a force parameter to forcefully disconne...

---
