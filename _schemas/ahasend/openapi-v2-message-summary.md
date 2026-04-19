---
description: MessageSummary schema from AhaSend API
layout: schema
name: MessageSummary
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: When the message was created
  name: created_at
  type: string
- description: When the message was last updated
  name: updated_at
  type: string
- description: When the message was sent
  name: sent_at
  type: string
- description: When the message was delivered
  name: delivered_at
  type: string
- description: When the message data will be purged
  name: retain_until
  type: string
- description: Message direction
  name: direction
  type: string
- description: Whether this is a bounce notification
  name: is_bounce_notification
  type: boolean
- description: Classification of bounce if applicable
  name: bounce_classification
  type: string
- description: List of delivery attempts for this message
  name: delivery_attempts
  type: array
- description: Message-ID header value
  name: message_id
  type: string
- description: API-generated message ID
  name: id
  type: string
- description: Message subject
  name: subject
  type: string
- description: Tags associated with the message
  name: tags
  type: array
- description: Sender email address
  name: sender
  type: string
- description: Recipient email address
  name: recipient
  type: string
- description: Current message status
  name: status
  type: string
- description: Number of delivery attempts
  name: num_attempts
  type: integer
- description: Number of clicks tracked for this message
  name: click_count
  type: integer
- description: Number of opens tracked for this message
  name: open_count
  type: integer
- description: ID of the original message (for bounce messages)
  name: reference_message_id
  type: integer
- description: Domain ID this message was sent from
  name: domain_id
  type: string
- description: Account ID this message belongs to
  name: account_id
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-message-summary-schema.json
slug: openapi-v2-message-summary
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: MessageSummary
---
