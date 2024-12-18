---
aid: github:github-projects-api
name: GitHub Projects API
tags:
  - Cards
  - Checks
  - Collaborators
  - Columns
  - Existing
  - Move
  - Moves
  - Organizations
  - Owners
  - Permission
  - Permissions
  - Projects
  - Repositories
  - Slug
  - Teams
  - User Names
  - Users
baseURL: https://api.github.com/
overlays:
  - url: overlays/github-projects-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-projects-openapi-original.yml
    type: OpenAPI
description: >-
  Use the REST API to create, list, update, delete and customize projects
  (classic).

---