---
description: WebhookConfig schema from AgeChecker.Net API
layout: schema
name: WebhookConfig
properties_list:
- description: Webhook configuration identifier.
  name: id
  type: string
- description: URL to receive webhook events.
  name: url
  type: string
- description: List of event types to receive.
  name: events
  type: array
- description: Shared secret for webhook signature verification.
  name: secret
  type: string
- description: When the webhook was configured.
  name: created_at
  type: string
provider_name: AgeChecker.Net
provider_slug: agechecker-net
schema_file: json-schema/age-verification-webhook-config-schema.json
slug: age-verification-webhook-config
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
title: WebhookConfig
---
