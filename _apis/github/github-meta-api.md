---
aid: github:github-meta-api
name: GitHub Meta API
tags: []
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/meta?apiVersion=2022-11-28
overlays:
  - url: overlays/github-meta--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-meta--openapi-original.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/meta
    type: Documentation
description: >-
  Use the REST API to get meta information about GitHub, including the IP
  addresses of GitHub services.

---