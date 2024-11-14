---
aid: stripe:stripe-application-fees-api
name: Stripe Application Fees API
tags:
  - Applications
  - Fees
  - Fee
  - Refunds
overlays:
  - url: overlays/application-fees-openapi-search.yml
    type: APIs.io Search
  - url: overlays/application-fees-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/application_fees
    type: Documentation
  - url: properties/application-fees-openapi-original.yml
    type: OpenAPI
description: >-
  When you collect a transaction fee on top of a charge made for your user
  (using Connect), an Application Fee object is created in your account. You can
  list, retrieve, and refund application fees.

---