---
aid: docker:docker-containerstart
name: Container Start
tags:
- Containers
- Start
humanURL: 
properties: []
description: >-
  This API operation starts a previously created Docker container identified by its unique container ID. When invoked via a POST request to the /containers/{id}/start endpoint, it initiates the container's main process and transitions the container from a created or stopped state to a running state. The operation accepts the container ID as a path parameter and may include optional configuration parameters in the request body, such as detach keys for detaching from the container. Upon successfu...

---
