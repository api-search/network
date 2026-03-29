---
aid: docker:docker-containerkill
name: Container Kill
tags:
- Containers
- Kill
humanURL: 
properties: []
description: >-
  Sends a signal to a running container identified by its ID, which by default is SIGKILL to immediately terminate the container, though other Unix signals can be specified via query parameters. This operation forcefully stops the container's main process without allowing it to gracefully shut down, which is useful when a container is unresponsive or needs to be stopped immediately. The endpoint requires the container ID in the path and returns a 204 No Content status on success, with error res...

---
