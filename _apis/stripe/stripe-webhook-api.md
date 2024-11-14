---
aid: stripe:stripe-webhook-api
name: Stripe Webhook API
tags:
  - Endpoints
  - Webhooks
overlays:
  - url: overlays/webhook-openapi-search.yml
    type: APIs.io Search
  - url: overlays/webhook-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/webhook_endpoints
    type: Documentation
  - url: properties/webhook-openapi-original.yml
    type: OpenAPI
description: >-
  You can configure webhook endpoints via the API to be notified about events
  that happen in your Stripe account or connected accounts.

---