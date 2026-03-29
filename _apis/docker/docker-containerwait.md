---
aid: docker:docker-containerwait
name: Container Wait
tags:
- Containers
- Wait
humanURL: 
properties: []
description: >-
  This API operation blocks and waits for a container to stop, then returns the exit code. When you make a POST request to this endpoint with a container ID, the call will not return until the specified container has finished executing and stopped. Once the container stops, the API responds with the container's exit code, which indicates whether the container completed successfully (typically 0) or encountered an error (non-zero value). This is particularly useful for synchronous workflows wher...

---
