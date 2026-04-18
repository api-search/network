---
description: Information about a configured webhook.
layout: schema
name: WebhookInfo
properties_list:
- description: The unique webhook identifier.
  name: id
  type: integer
- description: The webhook URL.
  name: url
  type: string
- description: A description of the webhook.
  name: description
  type: string
- description: The key used to generate webhook signatures for verifying webhook authenticity.
  name: auth_key
  type: string
- description: The events that trigger this webhook.
  name: events
  type: array
- description: When the webhook was created.
  name: created_at
  type: string
- description: When the webhook last fired.
  name: last_sent_at
  type: string
- description: Total number of event batches sent.
  name: batches_sent
  type: integer
- description: Total number of events sent.
  name: events_sent
  type: integer
- description: The last error received from the webhook URL.
  name: last_error
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-webhook-info-schema.json
slug: mailchimp-transactional-webhook-info
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: WebhookInfo
---
