---
aid: docker:docker-containerprune
name: Container Prune
tags:
- Containers
- Prune
humanURL: 
properties: []
description: >-
  The Container Prune API operation is a POST request to the `/containers/prune` endpoint that removes all stopped containers from the Docker host. This cleanup operation helps reclaim disk space by deleting containers that are no longer running and are not needed. You can optionally provide filters as query parameters to selectively prune containers based on specific criteria such as labels or time constraints. The operation returns a JSON response containing the list of deleted containers and...

---
