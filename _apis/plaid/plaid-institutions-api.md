---
aid: plaid:plaid-institutions-api
name: Plaid Institutions API
tags: []
score: 278
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/institutions/
overlays:
  - url: overlays/plaid-institutions--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-institutions--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-institutions--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/institutions/
    type: Documentation
description: >-
  Institutions endpoints support querying all institutions, as well as looking
  up a single institution to retrieve up-to-date information about its health
  status and capabilities. This can be useful for apps whose business logic may
  depend on institution capabilities, such as Payment Initiation. API-provided
  institution health data can also be used for in-app UIs.

---