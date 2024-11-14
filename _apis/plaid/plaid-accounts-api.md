---
aid: plaid:plaid-accounts-api
name: Plaid Accounts API
tags:
  - Accounts
  - Balance
  - Data
  - Real Time
score: 66
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/accounts/
overlays:
  - url: overlays/plaid-accounts--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-accounts--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-accounts--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/accounts/
    type: Documentation
description: >-
  API reference for retrieving account information and seeing all possible
  account types and subtypes

---