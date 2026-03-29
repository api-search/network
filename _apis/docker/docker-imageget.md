---
aid: docker:docker-imageget
name: Image Get
tags:
- Image
- Get
humanURL: 
properties: []
description: >-
  This API operation retrieves a Docker image and exports it as a tarball archive. By sending a GET request to the endpoint with a specific image name, the Docker daemon will package the specified image, including all of its layers and metadata, into a TAR format that can be saved to disk or transferred to another system. This is commonly used for backing up images, sharing them offline, or migrating images between different Docker environments without using a registry. The response is a binary...

---
