---
aid: plaid:plaid-link-api
name: Plaid Link API
tags:
  - Checks
  - Eligibility
  - Link
  - Profiles
  - Tokens
  - Correlation
  - Exchange
  - OAuth
score: 102
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/link/
overlays:
  - url: overlays/plaid-link--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-link--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-link--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/link/
    type: Documentation
description: Use Link to connect to your users' financial accounts with the Plaid API

---