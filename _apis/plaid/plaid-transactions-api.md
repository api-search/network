---
aid: plaid:plaid-transactions-api
name: Plaid Transactions API
tags: []
score: 1113
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/products/transactions/
overlays:
  - url: overlays/plaid-transactions--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-transactions--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-transactions--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/products/transactions/
    type: Documentation
description: >-
  Retrieve and refresh up to 24 months of historical transaction data, including
  geolocation, merchant, and category information.

---