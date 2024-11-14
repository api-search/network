---
aid: stripe:stripe-coupons-api
name: Stripe Coupons API
tags:
  - Coupons
overlays:
  - url: overlays/coupons-openapi-search.yml
    type: APIs.io Search
  - url: overlays/coupons-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/coupons
    type: Documentation
  - url: properties/coupons-openapi-original.yml
    type: OpenAPI
description: >-
  A coupon contains information about a percent-off or amount-off discount you
  might want to apply to a customer. Coupons may be applied to subscriptions,
  invoices, checkout sessions, quotes, and more. Coupons do not work with
  conventional one-off charges or payment intents.

---