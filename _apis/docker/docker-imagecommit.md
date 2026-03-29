---
aid: docker:docker-imagecommit
name: Image Commit
tags:
- Image
- Commits
humanURL: 
properties: []
description: >-
  This API operation creates a new Docker image from a container's changes by committing the current state of a specified container. When invoked via a POST request to the /commit endpoint, it captures all modifications made to a container's filesystem, configuration, and metadata, effectively saving them as a new image layer. The operation accepts parameters such as the container ID, repository name, tag, commit message, author information, and configuration changes to apply to the resulting i...

---
