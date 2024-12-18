---
aid: github:github-rate-limit-api
name: GitHub Rate Limit API
tags: []
baseURL: https://api.github.com/
humanURL: >-
  https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
overlays:
  - url: overlays/github-rate-limit--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-rate-limit--openapi-original.yml
    type: OpenAPI
description: >-
  Learn about REST API rate limits, how to avoid exceeding them, and what to do
  if you do exceed them.

---