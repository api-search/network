---
aid: stripe:stripe-disputes-api
name: Stripe Disputes API
tags:
  - Disputes
  - Close
overlays:
  - url: overlays/disputes-openapi-search.yml
    type: APIs.io Search
  - url: overlays/disputes-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/disputes
    type: Documentation
  - url: properties/disputes-openapi-original.yml
    type: OpenAPI
description: >-
  A dispute occurs when a customer questions your charge with their card issuer.
  When this happens, you have the opportunity to respond to the dispute with
  evidence that shows that the charge is legitimate.

---