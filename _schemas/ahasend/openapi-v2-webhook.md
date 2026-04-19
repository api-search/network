---
description: Webhook schema from AhaSend API
layout: schema
name: Webhook
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the webhook
  name: id
  type: string
- description: When the webhook was created
  name: created_at
  type: string
- description: When the webhook was last updated
  name: updated_at
  type: string
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
- description: Number of successful calls
  name: success_count
  type: integer
- description: Number of unsuccessful calls
  name: error_count
  type: integer
- description: Number of consecutive failed calls
  name: errors_since_last_success
  type: integer
- description: When the webhook was last called
  name: last_request_at
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-webhook-schema.json
slug: openapi-v2-webhook
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Webhook
---
