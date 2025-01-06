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
  - url: openapi/plaid-webhook-verification--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/webhooks/webhook-verification/
    type: Documentation
description: >-
  Plaid Webhook Verification API is a tool designed to help businesses verify
  the authenticity of webhook notifications sent by Plaid, a popular financial
  technology platform. This API allows businesses to confirm that the incoming
  webhook notifications are indeed from Plaid and have not been tampered with
  during transit. By verifying the signatures attached to the webhook
  notifications, businesses can ensure the integrity and security of their data
  and prevent potential fraud or unauthorized access to sensitive information.
  Additionally, the Plaid Webhook Verification API helps businesses maintain
  compliance with data protection regulations and build trust with their
  customers by providing a secure and reliable messaging system.

---