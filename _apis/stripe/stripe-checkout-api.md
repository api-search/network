---
aid: stripe:stripe-checkout-api
name: Stripe Checkout API
tags:
  - Checkout
  - Sessions
  - Expire
  - Items
  - Line
overlays:
  - url: overlays/checkout-openapi-search.yml
    type: APIs.io Search
  - url: overlays/checkout-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/payments/checkout
    type: Documentation
  - url: properties/checkout-openapi-original.yml
    type: OpenAPI
description: >-
  Checkout is a low-code payment integration that creates a customizable form
  for collecting payments. You can embed Checkout directly in your website or
  redirect customers to a Stripe-hosted payment page. It supports one-time
  payments and subscriptions and accepts over 40 local payment methods.

---