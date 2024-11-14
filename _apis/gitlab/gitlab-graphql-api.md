---
aid: gitlab:gitlab-graphql-api
name: GitLab GraphQL API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://docs.gitlab.com/ee/api/graphql/
overlays: []
properties:
  - url: https://docs.gitlab.com/ee/api/graphql/
    type: Documentation
  - url: https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
    type: Deprecation
  - url: https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
    type: Breaking Changes
  - url: https://docs.gitlab.com/ee/api/graphql/#limits
    type: Rate Limits
description: >-
  GraphQL is a query language for APIs. You can use it to request the exact data
  you need, and therefore limit the number of requests you need. GraphQL data is
  arranged in types, so your client can use client-side GraphQL libraries to
  consume the API and avoid manual parsing. There are no fixed endpoints and no
  data model, so you can add to the API without creating breaking changes. This
  enables us to have a versionless API.

---