---
aid: stripe:stripe-subscription-api
name: Stripe Subscription API
tags:
  - Items
  - Subscriptions
  - Record
  - Summaries
  - Usage
  - Records
  - Schedules
  - Cancel
  - Releases
  - Search
  - Exposed
  - Discount
  - Resume
overlays:
  - url: overlays/subscription-openapi-search.yml
    type: APIs.io Search
  - url: overlays/subscription-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/subscriptions
    type: Documentation
  - url: properties/subscription-openapi-original.yml
    type: OpenAPI
description: Subscriptions allow you to charge a customer on a recurring basis.

---