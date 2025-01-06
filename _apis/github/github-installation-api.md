---
aid: github:github-installation-api
name: GitHub Installation API
tags:
  - Access
  - Accessible
  - Applications
  - Authenticated
  - Installations
  - Organizations
  - Owners
  - Repositories
  - Revoke
  - Suspend
  - Suspended
  - Tokens
  - Unsuspend
  - User Names
  - Users
baseURL: https://api.github.com/
overlays:
  - url: overlays/github-installation-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-installation-openapi-original.yml
    type: OpenAPI
description: |-

  Use the REST API to get information about GitHub App installations and
  perform actions within those installations.

---