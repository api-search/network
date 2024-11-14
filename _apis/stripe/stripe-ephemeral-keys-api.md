---
aid: stripe:stripe-ephemeral-keys-api
name: Stripe Ephemeral Keys API
tags:
  - Ephemeral
  - Keys
overlays:
  - url: overlays/ephemeral-keys-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ephemeral-keys-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/issuing/elements
    type: Documentation
  - url: properties/ephemeral-keys-openapi-original.yml
    type: OpenAPI
description: >-
  Stripe.js uses ephemeral keys to securely retrieve Card information from the
  Stripe API without publicly exposing your secret keys. You need to do some of
  the ephemeral key exchange on the server-side to set this up.

---