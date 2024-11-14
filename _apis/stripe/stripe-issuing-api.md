---
aid: stripe:stripe-issuing-api
name: Stripe Issuing API
tags:
  - Authorization
  - Issuing
  - Approve
  - Decline
  - Card Holders
  - Cards
  - Disputes
  - Submit
  - Settlements
  - Tokens
  - Transactions
overlays:
  - url: overlays/issuing-openapi-search.yml
    type: APIs.io Search
  - url: overlays/issuing-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/issuing
    type: Documentation
  - url: properties/issuing-openapi-original.yml
    type: OpenAPI
description: >-
  An API for businesses to instantly create, manage, and distribute payment
  cards.

---