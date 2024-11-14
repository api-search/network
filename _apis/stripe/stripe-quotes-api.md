---
aid: stripe:stripe-quotes-api
name: Stripe Quotes API
tags:
  - Quotes
  - Accept
  - Cancel
  - Computed
  - Items
  - Line
  - Upfront
  - Finalize
  - PDF
overlays:
  - url: overlays/quotes-openapi-search.yml
    type: APIs.io Search
  - url: overlays/quotes-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/quotes
    type: Documentation
  - url: properties/quotes-openapi-original.yml
    type: OpenAPI
description: >-
  A Quote is a way to model prices that you'd like to provide to a customer.
  Once accepted, it will automatically create an invoice, subscription or
  subscription schedule.

---