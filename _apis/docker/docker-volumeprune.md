---
aid: docker:docker-volumeprune
name: Volume Prune
tags:
- Volume
- Prune
humanURL: 
properties: []
description: >-
  Removes all unused volumes from the Docker host, freeing up disk space by deleting volumes that are not currently referenced by any containers. This operation is irreversible and will permanently delete volume data, so it should be used with caution in production environments. The endpoint accepts optional filters to selectively prune volumes based on specific criteria such as labels or timestamps, and returns a detailed response including the list of deleted volumes and the total amount of d...

---
