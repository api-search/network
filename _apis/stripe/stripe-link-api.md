---
aid: stripe:stripe-link-api
name: Stripe Link API
tags:
  - Accounts
  - Link
  - Sessions
  - Linked
  - Disconnect
  - Owners
  - Refresh
overlays:
  - url: overlays/link-openapi-search.yml
    type: APIs.io Search
  - url: overlays/link-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/payment-links/api
    type: Documentation
  - url: properties/link-openapi-original.yml
    type: OpenAPI
description: >-
  You can use the Payment Links API to create a payment link that you can share
  with your customers. Stripe redirects customers who open this link to a
  Stripe-hosted payment page.

---