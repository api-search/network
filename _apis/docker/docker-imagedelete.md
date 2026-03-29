---
aid: docker:docker-imagedelete
name: Image Delete
tags:
- Image
- Delete
humanURL: 
properties: []
description: >-
  The Image Delete operation removes a Docker image from the local Docker host by specifying its name or ID in the path parameter. When invoked, this endpoint deletes the specified image along with its associated metadata, freeing up disk space on the system. The operation will fail if there are containers currently using the image or if the image has dependent child images, unless force deletion is specified through query parameters. Upon successful deletion, the API returns information about ...

---
