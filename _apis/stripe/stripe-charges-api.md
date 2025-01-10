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
properties:
  - url: https://stripe.com/docs/api/charges
    type: Documentation
  - url: openapi/charges-openapi-original.yml
    type: OpenAPI
description: >-
  The Charge object represents a single attempt to move money into your Stripe
  account. PaymentIntent confirmation is the most common way to create Charges,
  but transferring money to a different Stripe account through Connect also
  creates Charges. Some legacy payment flows create Charges directly, which is
  not recommended for new integrations.

---