---
aid: apis-io-rules:rules-api
name: APIs.io Rules API
tags:
  - Rules
image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-api-logo.jpg
rules:
  - url: https://github.com/api-search/rules-api
    type: GitHubRepository
  - url: >-
      https://github.com/api-search/rules-api/blob/main/.github/workflows/pipeline.yml
    type: GitHubActions
  - url: https://developer.apis.io/documentation/
    type: Documentation
  - url: https://github.com/api-search/rules-api/blob/main/rules/openapi.yml
    type: OpenAPI
baseURL: https://rules-api.apis.io
contact:
  - FN: APIs.io
    email: info@apis.io
humanURL: https://developer.apis.io/documentation
description: This is the API for powering APIs.io.

---