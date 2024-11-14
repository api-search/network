---
aid: stripe:stripe-invoice-api
name: Stripe Invoice API
tags:
  - Invoice Items
  - Invoices
  - Search
  - Upcoming
  - Lines
  - Finalize
  - Items
  - Line
  - Mark
  - Uncollectible
  - Pay
  - Send
overlays:
  - url: overlays/invoice-openapi-search.yml
    type: APIs.io Search
  - url: overlays/invoice-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/invoices
    type: Documentation
  - url: properties/invoice-openapi-original.yml
    type: OpenAPI
description: >-
  Invoices are statements of amounts owed by a customer, and are either
  generated one-off, or generated periodically from a subscription.

---