---
aid: stripe:stripe-payouts-api
name: Stripe Payouts API
tags:
  - Payouts
  - Cancel
  - Reverse
overlays:
  - url: overlays/payouts-openapi-search.yml
    type: APIs.io Search
  - url: overlays/payouts-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/payouts
    type: Documentation
  - url: properties/payouts-openapi-original.yml
    type: OpenAPI
description: >-
  A Payout object is created when you receive funds from Stripe, or when you
  initiate a payout to either a bank account or debit card of a connected Stripe
  account. You can retrieve individual payouts, and list all payouts. Payouts
  are made on varying schedules, depending on your country and industry.

---