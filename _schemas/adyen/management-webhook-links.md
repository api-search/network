---
description: WebhookLinks schema from Adyen API
layout: schema
name: WebhookLinks
properties_list:
- description: The company account that the webhook is configured for. Only present for company-level webhooks.
  name: company
  type: object
- description: Generate an HMAC key.
  name: generateHmac
  type: object
- description: The merchant account that the webhook is configured for. Only present for merchant-level webhooks.
  name: merchant
  type: object
- description: Link to the resource itself.
  name: self
  type: object
- description: Test the webhook setup.
  name: testWebhook
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhook-links-schema.json
slug: management-webhook-links
tags:
- Payments
- Financial Services
- Fintech
title: WebhookLinks
---
