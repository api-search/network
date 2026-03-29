---
aid: docker:docker-secretinspect
name: Secret Inspect
tags:
- Secrets
- Inspect
humanURL: 
properties: []
description: >-
  The Secret Inspect operation retrieves detailed information about a specific Docker secret by its unique identifier. This GET request is made to the `/secrets/{id}` endpoint where `{id}` is the secret's ID or name, and it returns comprehensive metadata about the secret including its specification, version information, creation and update timestamps, and labels, though the actual secret data itself remains encrypted and is not exposed through this endpoint. This operation is useful for adminis...

---
