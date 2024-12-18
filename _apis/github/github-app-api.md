---
aid: github:github-app-api
name: GitHub App API
tags:
  - Access
  - Actions
  - Applications
  - Approvals
  - Attempts
  - Authenticated
  - Authorization
  - Branch
  - Branches
  - Checks
  - Clients
  - Code
  - Configurations
  - Conversions
  - Deliveries
  - Git
  - Grants
  - History
  - Hook
  - Hub
  - Installations
  - Manifests
  - Owners
  - Protected
  - Protection
  - Redeliver
  - Repositories
  - Reset
  - Restrictions
  - Reviews
  - Runs
  - Scoped
  - Sets
  - Single
  - Slug
  - Suspend
  - Suspended
  - Tokens
  - Unsuspend
  - Webhooks
  - Workflows
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/rest/apps?apiVersion=2022-11-28
overlays:
  - url: overlays/github-app-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-app-openapi-original.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/apps
    type: Documentation
description: >-
  Use the REST API to retrieve information about GitHub Apps and GitHub App
  installations.

---