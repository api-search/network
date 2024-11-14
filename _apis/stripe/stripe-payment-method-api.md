---
aid: stripe:stripe-payment-method-api
name: Stripe Payment Method API
tags:
  - Configurations
  - Methods
  - Payments
  - Domains
  - Ate
  - Val
  - Validate
  - Attach
  - Detach
overlays:
  - url: overlays/payment-method-openapi-search.yml
    type: APIs.io Search
  - url: overlays/payment-method-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/payments/payment-methods
    type: Documentation
  - url: properties/payment-method-openapi-original.yml
    type: OpenAPI
description: >-
  The Payment Methods API allows you to accept a variety of payment methods
  through a single API. A PaymentMethod object contains the payment method
  details to create payments.

---