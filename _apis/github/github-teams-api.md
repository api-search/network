---
aid: github:github-teams-api
name: GitHub Teams API
tags:
  - Administrative
  - LDAP
  - Mapping
  - Teams
  - Sync
  - Managers
  - Organizations
  - Security
  - Slug
  - Removes
  - Names
  - Discussions
  - Discussion
  - Numbers
  - Comments
  - Reactions
  - Between
  - Connections
  - External
  - Groups
  - Members
  - Memberships
  - User Names
  - Users
  - Projects
  - Checks
  - Permissions
  - Repositories
  - Owners
  - Child
  - Access
  - Branch
  - Branches
  - Protected
  - Protection
  - Restrictions
  - Sets
  - (Legacy)
  - Authenticated
baseURL: https://api.github.com/
overlays:
  - url: overlays/github-teams-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-teams-openapi-original.yml
    type: OpenAPI
description: Needs description.

---