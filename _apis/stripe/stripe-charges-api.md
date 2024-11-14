---
aid: stripe:stripe-charges-api
name: Stripe Charges API
tags:
  - Charges
  - Search
  - Charge
  - Capture
  - Disputes
  - Close
  - Refunds
overlays:
  - url: overlays/charges-openapi-search.yml
    type: APIs.io Search
  - url: overlays/charges-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/charges
    type: Documentation
  - url: properties/charges-openapi-original.yml
    type: OpenAPI
description: >-
  The Charge object represents a single attempt to move money into your Stripe
  account. PaymentIntent confirmation is the most common way to create Charges,
  but transferring money to a different Stripe account through Connect also
  creates Charges. Some legacy payment flows create Charges directly, which is
  not recommended for new integrations.

---