---
description: UpdateWebhookRequest schema from AhaSend API
layout: schema
name: UpdateWebhookRequest
properties_list:
- description: Webhook name
  name: name
  type: string
- description: Webhook URL
  name: url
  type: string
- description: Whether the webhook is enabled
  name: enabled
  type: boolean
- description: Trigger on message reception
  name: on_reception
  type: boolean
- description: Trigger on message delivery
  name: on_delivered
  type: boolean
- description: Trigger on transient errors
  name: on_transient_error
  type: boolean
- description: Trigger on permanent failures
  name: on_failed
  type: boolean
- description: Trigger on bounces
  name: on_bounced
  type: boolean
- description: Trigger on suppressions
  name: on_suppressed
  type: boolean
- description: Trigger on opens
  name: on_opened
  type: boolean
- description: Trigger on clicks
  name: on_clicked
  type: boolean
- description: Trigger on suppression creation
  name: on_suppression_created
  type: boolean
- description: Trigger on DNS errors
  name: on_dns_error
  type: boolean
- description: Webhook scope
  name: scope
  type: string
- description: Domains this webhook applies to
  name: domains
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-update-webhook-request-schema.json
slug: openapi-v2-update-webhook-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: UpdateWebhookRequest
---
