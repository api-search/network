---
aid: github:github-code-of-conduct-api
name: GitHub Code of Conduct API
tags:
  - Keys
baseURL: https://api.github.com
humanURL: >-

  https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28
overlays:
  - url: overlays/github-codes-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-code-of-conduct-api-openapi.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct
    type: Documentation
description: Use the REST API to get information about codes of conduct.

---