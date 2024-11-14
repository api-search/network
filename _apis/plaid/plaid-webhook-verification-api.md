---
aid: plaid:plaid-webhook-verification-api
name: Plaid Webhook Verification API
tags: []
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/webhooks/webhook-verification/
overlays:
  - url: overlays/plaid-webhook-verification--openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/plaid-webhook-verification--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/webhooks/webhook-verification/
    type: Documentation
description: >-
  Plaid signs all outgoing webhooks so that you can verify the authenticity of
  any incoming webhooks to your application. 

---