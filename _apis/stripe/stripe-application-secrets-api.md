---
aid: stripe:stripe-application-secrets-api
name: Stripe Application Secrets API
tags:
  - Applications
  - Secrets
  - Find
overlays:
  - url: overlays/application-secrets-openapi-search.yml
    type: APIs.io Search
  - url: overlays/application-secrets-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/secret_management
    type: Documentation
  - url: properties/application-secrets-openapi-original.yml
    type: OpenAPI
description: >-
  Secret Store is an API that allows Stripe Apps developers to securely persist
  secrets for use by UI Extensions and app backends.

---