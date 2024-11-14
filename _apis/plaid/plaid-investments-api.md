---
aid: plaid:plaid-investments-api
name: Plaid Investments API
tags:
  - Holdings
  - Investments
  - Transactions
  - Data
  - Refresh
  - Authentication
  - Authorize
  - Needed
  - Transfers
score: 109
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/investments/
overlays:
  - url: overlays/plaid-investments--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-investments--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-investments--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/investments/
    type: Documentation
description: Needs descriptionView holdings and transactions from investment accounts.

---