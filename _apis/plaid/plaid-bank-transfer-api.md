---
aid: plaid:plaid-bank-transfer-api
name: Plaid Bank Transfer API
tags:
  - Bank
  - Processor
  - Transfers
  - Cancels
  - Events
  - Sync
  - Sweep
  - Sweeps
  - Accounts
  - Balance
  - Migrate
  - Sandbox
  - Simulate
  - Fire
  - Manually
  - Webhooks
score: 372
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/products/transfer/
overlays:
  - url: overlays/plaid-bank-transfer--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-bank-transfer--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-bank-transfer--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/products/transfer/
    type: Documentation
description: API reference for Transfer endpoints and webhooks.

---