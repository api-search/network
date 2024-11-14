---
aid: stripe:stripe-exchange-rates-api
name: Stripe Exchange Rates API
tags:
  - Exchange
  - Rates
overlays:
  - url: overlays/exchange-rates-openapi-search.yml
    type: APIs.io Search
  - url: overlays/exchange-rates-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/currencies/conversions
    type: Documentation
  - url: properties/exchange-rates-openapi-original.yml
    type: OpenAPI
description: >-
  Stripe supports processing charges in 135+ currencies allowing you to present
  prices in a customer's native currency. Doing so can improve sales and help
  customers avoid conversion costs. In order to present prices in your
  customer's currency, you need to specify the presentment currency when
  creating a PaymentIntent or a charge.

---