---
aid: plaid:plaid-sandbox-api
name: Plaid Sandbox API
tags: []
score: 635
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/sandbox/
overlays:
  - url: overlays/plaid-sandbox--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-sandbox--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-sandbox--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/sandbox/
    type: Documentation
description: >-
  The Plaid Sandbox is a free and fully-featured environment for application
  development and testing. All Plaid functionality of both the Plaid API and
  Plaid Link is supported in the Sandbox environment. 

---