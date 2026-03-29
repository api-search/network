---
aid: docker:docker-containerstop
name: Container Stop
tags:
- Containers
- Stop
humanURL: 
properties: []
description: >-
  This API operation stops a running Docker container identified by its unique container ID provided in the URL path. When invoked via a POST request to the endpoint /containers/{id}/stop, it sends a SIGTERM signal to the container's main process, allowing it to gracefully shut down. The operation accepts an optional query parameter 't' to specify the number of seconds to wait before forcefully killing the container with SIGKILL if it hasn't stopped gracefully. Upon successful execution, the AP...

---
