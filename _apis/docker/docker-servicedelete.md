---
aid: docker:docker-servicedelete
name: Service Delete
tags:
- Services
- Delete
humanURL: 
properties: []
description: >-
  Deletes a Docker service by its unique identifier. This operation removes the specified service from the Docker Swarm cluster, stopping all running tasks and containers associated with it. The service ID must be provided in the URL path as a required parameter. Once deleted, the service and its configuration are permanently removed from the cluster, though any volumes or networks created separately may need to be cleaned up independently. This is a destructive operation that cannot be undone,...

---
