---
aid: stripe:stripe-tokens-api
name: Stripe Tokens API
tags:
  - Tokens
overlays:
  - url: overlays/tokens-openapi-search.yml
    type: APIs.io Search
  - url: overlays/tokens-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/tokens
    type: Documentation
  - url: properties/tokens-openapi-original.yml
    type: OpenAPI
description: >-
  Tokenization is the process Stripe uses to collect sensitive card or bank
  account details, or personally identifiable information (PII), directly from
  your customers in a secure manner. A token representing this information is
  returned to your server to use. Use our recommended payments integrations to
  perform this process on the client-side. This guarantees that no sensitive
  card data touches your server, and allows your integration to operate in a
  PCI-compliant way.

---