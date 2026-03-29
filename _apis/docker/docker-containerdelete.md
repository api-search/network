---
aid: docker:docker-containerdelete
name: Container Delete
tags:
- Containers
- Delete
humanURL: 
properties: []
description: >-
  This API operation removes a specified Docker container from the system by sending a DELETE request to the /containers/{id} endpoint, where {id} is the unique identifier or name of the container. The operation permanently deletes the container instance, including its filesystem and metadata, but does not remove the container's image or associated volumes by default unless specifically configured to do so through query parameters. This endpoint is typically used when a container is no longer n...

---
