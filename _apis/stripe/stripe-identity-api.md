---
aid: stripe:stripe-identity-api
name: Stripe Identity API
tags:
  - Entities
  - Identity
  - Reports
  - Verification
  - Sessions
  - Cancel
  - Redact
overlays:
  - url: overlays/identity-openapi-search.yml
    type: APIs.io Search
  - url: overlays/identity-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/identity
    type: Documentation
  - url: properties/identity-openapi-original.yml
    type: OpenAPI
description: >-
  Use Stripe Identity to confirm the identity of global users to prevent fraud,
  streamline risk operations, and increase trust and safety.

---