---
aid: stripe:stripe-apple-pay-api
name: Stripe Apple Pay API
tags:
  - Apple
  - Domains
  - Pay
overlays:
  - url: overlays/apple-pay-openapi-search.yml
    type: APIs.io Search
  - url: overlays/apple-pay-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/apple-pay
    type: Documentation
  - url: properties/apple-pay-openapi-original.yml
    type: OpenAPI
description: >-
  Stripe users can accept Apple Pay in iOS applications in iOS 9 and above, and
  on the web in Safari starting with iOS 10 or macOS Sierra. There are no
  additional fees to process Apple Pay payments, and the pricing is the same as
  other card transactions.

---