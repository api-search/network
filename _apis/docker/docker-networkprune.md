---
aid: docker:docker-networkprune
name: Network Prune
tags:
- Network
- Prune
humanURL: 
properties: []
description: >-
  This API operation removes all unused networks from the Docker host by sending a POST request to the /networks/prune endpoint. When executed, it deletes networks that are not currently being used by any containers, helping to free up system resources and clean up dangling network configurations. The operation accepts optional filters as query parameters to selectively prune networks based on specific criteria such as labels or creation time, and returns a list of the networks that were succes...

---
