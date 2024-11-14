---
aid: plaid:plaid-liabilities-api
name: Plaid Liabilities API
tags:
  - Data
  - Liabilities
  - Processor
score: 60
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/products/liabilities/
overlays:
  - url: overlays/plaid-liabilities--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-liabilities--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-liabilities--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/products/liabilities/
    type: Documentation
description: API reference for Liabilities endpoints and webhooks.

---