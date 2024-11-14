---
aid: stripe:stripe-payment-intents-api
name: Stripe Payment Intents API
tags:
  - Intents
  - Payments
  - Search
  - Intent
  - Balance
  - Customers
  - Cancel
  - Capture
  - Confirm
  - Authorization
  - Increment
  - Microdeposits
  - Verify
overlays:
  - url: overlays/payment-intents-openapi-search.yml
    type: APIs.io Search
  - url: overlays/payment-intents-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/payment_intents
    type: Documentation
  - url: properties/payment-intents-openapi-original.yml
    type: OpenAPI
description: >-
  A PaymentIntent guides you through the process of collecting a payment from
  your customer. We recommend that you create exactly one PaymentIntent for each
  order or customer session in your system. You can reference the PaymentIntent
  later to see the history of payment attempts for a particular session.

---