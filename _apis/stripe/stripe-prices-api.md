---
aid: stripe:stripe-prices-api
name: Stripe Prices API
tags:
  - Prices
  - Search
overlays:
  - url: overlays/prices-openapi-search.yml
    type: APIs.io Search
  - url: overlays/prices-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/prices
    type: Documentation
  - url: properties/prices-openapi-original.yml
    type: OpenAPI
description: >-
  Prices define the unit cost, currency, and (optional) billing cycle for both
  recurring and one-time purchases of products. Products help you track
  inventory or provisioning, and prices help you track payment terms. Different
  physical goods or levels of service should be represented by products, and
  pricing options should be represented by prices. This approach lets you change
  prices without having to change your provisioning scheme.

---