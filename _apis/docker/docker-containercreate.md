---
aid: docker:docker-containercreate
name: Container Create
tags:
- Containers
- Create
humanURL: 
properties: []
description: >-
  Creates a new container from a specified Docker image without starting it. This operation accepts a JSON body with configuration parameters including the image name, environment variables, port bindings, volume mounts, network settings, and resource constraints. The container is assigned a unique ID upon creation and remains in a stopped state until explicitly started with a separate API call. This endpoint is commonly used to prepare containers with specific configurations before execution, ...

---
