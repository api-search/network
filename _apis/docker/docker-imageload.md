---
aid: docker:docker-imageload
name: Image Load
tags:
- Image
- Load
humanURL: 
properties: []
description: >-
  The Docker POST /images/load API operation allows users to load a tarball containing one or more Docker images into the Docker daemon's local image store. This endpoint accepts a tar archive (optionally compressed with gzip, bzip2, or xz) in the request body, which typically contains image layers and metadata exported from another Docker instance using the save command. When invoked, Docker extracts the archive and reconstructs the images with their associated tags, making them available for ...

---
