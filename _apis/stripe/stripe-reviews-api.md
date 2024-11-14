---
aid: stripe:stripe-reviews-api
name: Stripe Reviews API
tags:
  - Reviews
  - Approve
overlays:
  - url: overlays/reviews-openapi-search.yml
    type: APIs.io Search
  - url: overlays/reviews-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/radar/reviews
    type: Documentation
  - url: properties/reviews-openapi-original.yml
    type: OpenAPI
description: >-
  Reviews can be used to supplement automated fraud detection with human
  expertise.

---