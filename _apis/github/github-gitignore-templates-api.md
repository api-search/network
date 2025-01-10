---
aid: github:github-gitignore-templates-api
name: GitHub Gitignore Templates API
tags:
  - Git Ignore
  - Names
  - Templates
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28
overlays:
  - url: overlays/github-gitignore-templates--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-gitignore-templates--openapi-original.yml
    type: OpenAPI
description: |-

  Use the REST API to get .gitignore templates that can be used to ignore
  files and directories.

---