---
aid: github:github-events-api
name: GitHub Events API
tags:
  - Authenticated
  - Events
  - Issues
  - Organizations
  - Owners
  - Public
  - Repositories
  - User Names
  - Users
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
overlays:
  - url: overlays/github-events--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-events--openapi-original.yml
    type: OpenAPI
description: Use the REST API to interact with GitHub events.

---