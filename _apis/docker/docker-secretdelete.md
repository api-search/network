---
aid: docker:docker-secretdelete
name: Secret Delete
tags:
- Secrets
- Delete
humanURL: 
properties: []
description: >-
  This API operation deletes a specific Docker secret identified by its unique ID. When invoked, it removes the secret from the Docker Swarm, making it permanently unavailable to any services or containers that might have been using it. The operation requires the secret ID to be provided in the URL path parameter and typically returns a success status when the deletion is completed. This is a destructive action that cannot be undone, so the secret data will be irrecoverably removed from the sys...

---
