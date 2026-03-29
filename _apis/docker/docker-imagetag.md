---
aid: docker:docker-imagetag
name: Image Tag
tags:
- Image
- Tags
humanURL: 
properties: []
description: >-
  This API operation tags an existing Docker image with a new name and optional tag, creating an additional reference to the same image without duplicating the image data. By sending a POST request to /images/{name}/tag with the image name or ID and specifying the target repository and tag as query parameters, you can create a new alias for an image, which is useful for versioning, organizing images across different repositories, or preparing images for pushing to a registry. The operation does...

---
