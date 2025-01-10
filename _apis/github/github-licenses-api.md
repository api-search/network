---
aid: github:github-licenses-api
name: GitHub Licenses API
tags:
  - Licenses
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28
overlays:
  - url: overlays/github-licenses--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-licenses--openapi-original.yml
    type: OpenAPI
description: |-

  Use the REST API to retrieve popular open source licenses and information
  about a particular project's license file.

---