---
aid: github:github-feeds-api
name: GitHub Feeds API
tags: []
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28
overlays:
  - url: overlays/github-feeds--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/github-feeds--openapi-original.yml
    type: OpenAPI
description: >-
  Use the REST API to interact with GitHub feeds. Lists the feeds available to
  the authenticated user. The response provides a URL for each feed. You can
  then get a specific feed by sending a request to one of the feed URLs.

---