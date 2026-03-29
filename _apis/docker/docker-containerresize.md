---
aid: docker:docker-containerresize
name: Container Resize
tags:
- Containers
- Resize
humanURL: 
properties: []
description: >-
  This API operation resizes the TTY (terminal) dimensions for a specified Docker container by sending a POST request to the /containers/{id}/resize endpoint, where {id} is the container identifier. It accepts query parameters for height and width to adjust the pseudo-terminal size of the container's console, which is particularly useful when working with interactive containers that have a TTY allocated. The operation allows developers and administrators to dynamically adjust terminal dimension...

---
