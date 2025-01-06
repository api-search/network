---
aid: github:github-enterprise-api
name: GitHub Enterprise API
tags: []
baseURL: https://api.github.com
humanURL: https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin
overlays:
  - url: overlays/github-enterprise-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-enterprise-openapi-original.yml
    type: OpenAPI
  - url: |-

      https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin
    type: Documentation
description: |-

  Create integrations, retrieve data, and automate your workflows with the
  GitHub REST API.

---