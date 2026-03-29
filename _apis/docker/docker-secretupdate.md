---
aid: docker:docker-secretupdate
name: Secret Update
tags:
- Secrets
- Update
humanURL: 
properties: []
description: >-
  Updates a secret with a new version. This operation requires the secret ID and the current version number specified in the query parameters. The secret must exist and the version number must match the current version of the secret. The request body should contain the new secret data and optional metadata such as name, labels, or driver configuration. Upon successful update, the secret version is incremented and a new secret object is returned. This is useful for rotating credentials or updati...

---
