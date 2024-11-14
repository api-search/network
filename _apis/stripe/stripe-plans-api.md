---
aid: stripe:stripe-plans-api
name: Stripe Plans API
tags:
  - Plans
  - Plan
overlays:
  - url: overlays/plans-openapi-search.yml
    type: APIs.io Search
  - url: overlays/plans-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/plans
    type: Documentation
  - url: properties/plans-openapi-original.yml
    type: OpenAPI
description: >-
  You can now model subscriptions more flexibly using the Prices API. It
  replaces the Plans API and is backwards compatible to simplify your migration.

---