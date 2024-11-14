---
aid: stripe:stripe-events-api
name: Stripe Events API
tags:
  - Events
overlays:
  - url: overlays/events-openapi-search.yml
    type: APIs.io Search
  - url: overlays/events-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/events
    type: Documentation
  - url: properties/events-openapi-original.yml
    type: OpenAPI
description: >-
  Events are our way of letting you know when something interesting happens in
  your account. When an interesting event occurs, we create a new Event object.

---