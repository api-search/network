---
aid: stripe:stripe-balance-api
name: Stripe Balance API
tags:
  - Balance
  - History
  - Transactions
overlays:
  - url: overlays/balance-openapi-search.yml
    type: APIs.io Search
  - url: overlays/balance-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/balance
    type: Documentation
  - url: properties/balance-openapi-original.yml
    type: OpenAPI
description: >-
  This is an object representing your Stripe balance. You can retrieve it to see
  the balance currently on your Stripe account. You can also retrieve the
  balance history, which contains a list of transactions that contributed to the
  balance (charges, payouts, and so forth).

---