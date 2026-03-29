---
aid: docker:docker-imagecreate
name: Image Create
tags:
- Image
- Create
humanURL: 
properties: []
description: >-
  The POST /images/create endpoint is used to pull or import Docker images into the local Docker environment. This operation allows you to create a new image by pulling it from a registry (like Docker Hub) or importing it from a tarball. You can specify the image name and tag through query parameters, and the endpoint supports authentication for private registries. The operation returns a stream of JSON objects that provide status updates during the pull or import process, including progress in...

---
