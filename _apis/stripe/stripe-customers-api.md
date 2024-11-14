---
aid: stripe:stripe-customers-api
name: Stripe Customers API
tags:
  - Customers
  - Search
  - Balance
  - Transactions
  - Accounts
  - Bank
  - Verify
  - Cards
  - Cash
  - Discount
  - Funding
  - Instructions
  - Methods
  - Payments
  - Sources
  - Subscriptions
  - Exposed
  - Ids
  - Taxes
overlays:
  - url: overlays/customers-openapi-search.yml
    type: APIs.io Search
  - url: overlays/customers-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/customers
    type: Documentation
  - url: properties/customers-openapi-original.yml
    type: OpenAPI
description: >-
  This object represents a customer of your business. Use it to create recurring
  charges and track payments that belong to the same customer.

---