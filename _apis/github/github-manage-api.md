---
aid: github:github-manage-api
name: GitHub Manage API
tags:
  - Configurations
  - GHES
  - Manage
  - Metadata
  - Nodes
  - Releases
  - Replicas
  - Replication
  - Running
  - Services
  - Status
  - Versions
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
overlays:
  - url: overlays/github-manage-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-manage-openapi-original.yml
    type: OpenAPI
description: Needs description.

---