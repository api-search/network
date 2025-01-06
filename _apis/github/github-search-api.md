---
aid: github:github-search-api
name: GitHub Search API
tags:
  - Code
  - Search
  - Commits
  - Issues
  - Pull
  - Labels
  - Repositories
  - Topics
  - Users
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
overlays:
  - url: overlays/github-search-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-search-openapi-original.yml
    type: OpenAPI
description: Use the REST API to search for specific items on GitHub.

---