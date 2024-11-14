---
aid: stripe:stripe-topups-api
name: Stripe Topups API
tags:
  - Topups
  - Cancel
overlays:
  - url: overlays/topups-openapi-search.yml
    type: APIs.io Search
  - url: overlays/topups-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/topups
    type: Documentation
  - url: properties/topups-openapi-original.yml
    type: OpenAPI
description: >-
  To top up your Stripe balance, you create a top-up object. You can retrieve
  individual top-ups, as well as list all top-ups. Top-ups are identified by a
  unique, random ID.

---