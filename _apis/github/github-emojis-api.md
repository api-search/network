---
aid: github:github-emojis-api
name: GitHub Emojis API
tags: []
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28
overlays:
  - url: overlays/github-emojis--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-emojis--openapi-original.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/emojis
    type: Documentation
description: Use the REST API to list and view all the available emojis to use on GitHub.

---