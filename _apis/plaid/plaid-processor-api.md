---
aid: plaid:plaid-processor-api
name: Plaid Processor API
tags:
  - Authentication
  - Data
  - Processor
  - Accounts
  - Associated
  - Tokens
  - Transactions
  - Incremental
  - Sync
  - Refresh
  - Fetch
  - Recurring
  - Streams
  - ACH
  - Evaluate
  - Planned
  - Signals
  - Decision
  - Initiated
  - Reports
  - Whether
  - Opt In
  - Prepare
  - Bank
  - Transfers
  - Liabilities
  - Entities
  - Identity
  - Match
  - Scores
  - Balance
  - Access
  - Controls
  - Permissions
  - Processor's
  - Products
  - Sets
  - Token's
  - URL
  - Webhooks
  - Stripe
  - Apex
score: 529
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/processor-partners/
overlays:
  - url: overlays/plaid-processor--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-processor--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-processor--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/processor-partners/
    type: Documentation
description: >-
  Partner processor endpoints are used by Plaid partners to integrate with
  Plaid. Instead of using an access_token associated with a Plaid Item, these
  endpoints use a processor_token to identify a single financial account. 

---