---
aid: github:github-auth-api
name: GitHub Auth API
tags:
  - Administrative
  - Applications
  - Authorization
  - Authorized
  - Clients
  - Existing
  - Fingerprint
  - Impersonation
  - Keys
  - OAuth
  - SSH
  - Settings
  - Setup
  - Single
  - Specific
  - Tokens
  - User Names
  - Users
baseURL: https://api.github.com
humanURL: >-
  https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
overlays:
  - url: overlays/github-auth-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-auth-openapi-original.yml
    type: OpenAPI
  - url: >-
      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
    type: Documentation
description: >-
  You can authenticate to the REST API to access more endpoints and have a
  higher rate limit.

---