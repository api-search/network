---
aid: stripe:stripe-payment-links-api
name: Stripe Payment Links API
tags:
  - Links
  - Payments
  - Link
  - Items
  - Line
overlays:
  - url: overlays/payment-links-openapi-search.yml
    type: APIs.io Search
  - url: overlays/payment-links-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/payment_links/payment_links
    type: Documentation
  - url: properties/payment-links-openapi-original.yml
    type: OpenAPI
description: >-
  A payment link is a shareable URL that will take your customers to a hosted
  payment page. A payment link can be shared and used multiple times. When a
  customer opens a payment link it will open a new checkout session to render
  the payment page. You can use checkout session events to track payments
  through payment links.

---