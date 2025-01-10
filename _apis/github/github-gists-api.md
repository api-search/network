---
aid: github:github-gists-api
name: GitHub Gists API
tags:
  - Checks
  - Comments
  - Commits
  - Fork
  - Forks
  - Gists
  - Public
  - Revisions
  - SHA
  - Star
  - Starred
  - Unstar
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/gists?apiVersion=2022-11-28
overlays:
  - url: overlays/github-gists--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-gists--openapi-original.yml
    type: OpenAPI
description: |-

  Use the REST API to list, create, update and delete the public gists on
  GitHub.

---