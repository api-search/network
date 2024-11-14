---
aid: stripe:stripe-refunds-api
name: Stripe Refunds API
tags:
  - Refunds
  - Cancel
overlays:
  - url: overlays/refunds-openapi-search.yml
    type: APIs.io Search
  - url: overlays/refunds-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/refunds
    type: Documentation
  - url: properties/refunds-openapi-original.yml
    type: OpenAPI
description: >-
  Refund objects allow you to refund a previously created charge that isn't
  refunded yet. Funds are refunded to the credit or debit card that's initially
  charged.

---