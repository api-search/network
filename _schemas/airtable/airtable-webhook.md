---
description: An Airtable webhook subscription that monitors a base for changes and sends notifications to a specified URL. Webhooks expire after 7 days and must be periodically refreshed.
layout: schema
name: Airtable Webhook
properties_list:
- description: The unique identifier for the webhook.
  name: id
  type: string
- description: The type of webhook (e.g., client).
  name: type
  type: string
- description: Whether the webhook is currently active and will process events.
  name: isHookEnabled
  type: boolean
- description: The URL that receives POST notifications when monitored changes occur.
  name: notificationUrl
  type:
  - string
  - 'null'
- description: The cursor position indicating the next unread payload. Used when polling for payloads.
  name: cursorForNextPayload
  type: integer
- description: Whether HTTP notifications are currently being sent to the notification URL.
  name: areNotificationsEnabled
  type: boolean
- description: The time when the webhook was created.
  name: createdTime
  type: string
- description: The time when the webhook will expire if not refreshed. Webhooks expire 7 days after creation or last refresh.
  name: expirationTime
  type: string
- description: The specification defining which changes the webhook monitors, including data types, field filters, and source options.
  name: specification
  type: object
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-webhook-schema.json
slug: airtable-webhook
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Webhook
---
