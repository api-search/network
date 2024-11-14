---
aid: stripe:stripe-transfers-api
name: Stripe Transfers API
tags:
  - Transfers
  - Reversals
overlays:
  - url: overlays/transfers-openapi-search.yml
    type: APIs.io Search
  - url: overlays/transfers-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/transfers
    type: Documentation
  - url: properties/transfers-openapi-original.yml
    type: OpenAPI
description: >-
  A Transfer object is created when you move funds between Stripe accounts as
  part of Connect.

---