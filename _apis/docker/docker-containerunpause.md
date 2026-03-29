---
aid: docker:docker-containerunpause
name: Container Unpause
tags:
- Containers
humanURL: 
properties: []
description: >-
  Unpauses a container that was previously paused using the pause endpoint. This operation resumes all processes that were frozen within the specified container, allowing the container to continue executing from the exact state where it was paused. The container ID or name must be provided in the path parameter. When successful, the API returns a 204 No Content response indicating the container has been successfully unpaused. If the container is not found, a 404 error is returned, and if the co...

---
