---
aid: etcd:etcd-authauthenticate
name: Authenticate a user
tags:
- Auth
humanURL: 
properties: []
description: >-
  Authenticates a user with their username and password and returns a JWT token that can be used for subsequent authenticated requests. The token must be included in the Authorization header as a Bearer token. Tokens expire based on the cluster's configured token TTL and must be refreshed by calling this endpoint again.

---
