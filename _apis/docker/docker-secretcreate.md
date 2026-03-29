---
aid: docker:docker-secretcreate
name: Secret Create
tags:
- Secrets
- Create
humanURL: 
properties: []
description: >-
  This API operation creates a new secret in Docker Swarm mode by sending a POST request to the /secrets/create endpoint. Secrets are sensitive data such as passwords, SSH private keys, SSL certificates, or any other data that should not be stored unencrypted in a Dockerfile or application source code. When creating a secret, you provide the secret data along with metadata such as the secret name and optional labels. The secret data is encrypted during transit and at rest within the Docker Swar...

---
