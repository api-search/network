---
aid: stripe:stripe-sources-api
name: Stripe Sources API
tags:
  - Sources
  - Mandate
  - Notifications
  - Transactions
  - Verify
overlays:
  - url: overlays/sources-openapi-search.yml
    type: APIs.io Search
  - url: overlays/sources-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/sources
    type: Documentation
  - url: properties/sources-openapi-original.yml
    type: OpenAPI
description: >-
  Source objects allow you to accept a variety of payment methods. They
  represent a customer's payment instrument, and can be used with the Stripe API
  just like a Card object once chargeable, they can be charged, or can be
  attached to customers.

---