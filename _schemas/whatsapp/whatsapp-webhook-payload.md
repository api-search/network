---
description: Schema for incoming WhatsApp Business Platform webhook payloads. All webhook notifications follow a common envelope structure with event-specific data in the changes array.
layout: schema
name: WhatsApp Webhook Payload
properties_list:
- description: Always 'whatsapp_business_account' for WhatsApp webhooks
  name: object
  type: string
- description: ''
  name: entry
  type: array
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-webhook-payload-schema.json
slug: whatsapp-webhook-payload
tags: []
title: WhatsApp Webhook Payload
---
