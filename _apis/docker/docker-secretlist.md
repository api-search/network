---
aid: docker:docker-secretlist
name: Secret List
tags:
- Secrets
- Lists
humanURL: 
properties: []
description: >-
  Returns a list of secrets stored in the Docker Swarm cluster. This endpoint retrieves metadata about all secrets that the authenticated user has access to, including their ID, version, creation and update timestamps, and specification details. Secrets in Docker Swarm are used to securely store and manage sensitive data such as passwords, API keys, and certificates that can be made available to services. The response includes an array of secret objects, but does not return the actual secret da...

---
