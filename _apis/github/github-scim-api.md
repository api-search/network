---
aid: github:github-scim-api
name: GitHub SCIM API
tags:
  - Attributes
  - Enterprise
  - Groups
  - Identities
  - Information
  - Provision
  - Provisioned
  - Provisioning
  - SCIM
  - Sets
  - Users
baseURL: https://api.github.com/
humanURL: >-

  https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28
overlays:
  - url: overlays/github-scim-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-scim-openapi-original.yml
    type: OpenAPI
description: |-

  Use the REST API to control and manage your GitHub organization members'
  access with SCIM.

---