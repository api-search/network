---
aid: github:github-app-api
name: GitHub App API
tags:
  - Applications
  - Manifests
  - Code
  - Conversions
  - Hook
  - Configurations
  - Deliveries
  - Attempts
  - Installation
  - Installations
  - Access_tokens
  - Suspended
  - Grants
  - Grants""
  - Token
  - Scoped
  - App_slug
  - Repositories
  - Owner
  - Actions
  - Runs
  - Approvals
  - Branches
  - Branch
  - Protection
  - Restrictions
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/rest/apps?apiVersion=2022-11-28
overlays:
  - url: overlays/github-app-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-app-api-openapi.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/apps
    type: Documentation
description: |-

  Use the REST API to retrieve information about GitHub Apps and GitHub App
  installations.

---