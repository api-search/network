---
aid: github:github-notifications-api
name: GitHub Notifications API
tags:
  - Notifications
  - Threads
  - Mark
  - Read
  - Authenticated
  - Subscriptions
  - Users
  - Sets
baseURL: https://api.github.com/
humanURL: |-

  https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28
overlays:
  - url: overlays/github-notifications--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-notifications--openapi-original.yml
    type: OpenAPI
description: |+

  Use the REST API to manage GitHub notifications.




---