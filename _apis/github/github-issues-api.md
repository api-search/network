---
aid: github:github-issues-api
name: GitHub Issues API
tags:
  - Assigned
  - Assignee
  - Assignees
  - Checks
  - Comments
  - Events
  - Issues
  - Labels
  - Locks
  - Names
  - Numbers
  - Owners
  - Reactions
  - Repositories
  - Sets
  - Timeline
  - Unlock
  - Users
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/issues?apiVersion=2022-11-28
overlays:
  - url: overlays/github-issues--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-issues--openapi-original.yml
    type: OpenAPI
description: >-
  Use the REST API to view and manage issues, including issue assignees,
  comments, labels, and milestones.

---