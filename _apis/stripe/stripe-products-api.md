---
aid: stripe:stripe-products-api
name: Stripe Products API
tags:
  - Products
  - Search
overlays:
  - url: overlays/products-openapi-search.yml
    type: APIs.io Search
  - url: overlays/products-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/products
    type: Documentation
  - url: properties/products-openapi-original.yml
    type: OpenAPI
description: >-
  Products describe the specific goods or services you offer to your customers.
  For example, you might offer a Standard and Premium version of your goods or
  service; each version would be a separate Product. They can be used in
  conjunction with Prices to configure pricing in Payment Links, Checkout, and
  Subscriptions.

---