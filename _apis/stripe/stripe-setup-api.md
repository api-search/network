---
aid: stripe:stripe-setup-api
name: Stripe Setup API
tags:
  - Attempts
  - Setup
  - Intents
  - Intent
  - Cancel
  - Confirm
  - Microdeposits
  - Verify
overlays:
  - url: overlays/setup-openapi-search.yml
    type: APIs.io Search
  - url: overlays/setup-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/payments/setup-intents
    type: Documentation
  - url: properties/setup-openapi-original.yml
    type: OpenAPI
description: >-
  Use the Setup Intents API to set up a payment method for future payments. It's
  similar to a payment, but no charge is created. Set up a payment method for
  future payments now.

---