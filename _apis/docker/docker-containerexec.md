---
aid: docker:docker-containerexec
name: Container Exec
tags:
- Containers
humanURL: 
properties: []
description: >-
  This API operation creates an exec instance within a specified Docker container, allowing you to run commands inside an already running container without starting a new container or attaching to the existing process. By sending a POST request to /containers/{id}/exec with the container ID, you can specify the command to execute along with configuration options such as whether to attach to stdin/stdout/stderr, set environment variables, define the working directory, and configure user permissi...

---
