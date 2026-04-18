---
description: Schema for outbound WhatsApp messages sent via the Cloud API POST /{phone-number-id}/messages endpoint. Covers all message types including text, media, location, contacts, interactive, template, and reaction messages.
layout: schema
name: WhatsApp Message
properties_list:
- description: Must be 'whatsapp'
  name: messaging_product
  type: string
- description: Recipient type, currently only 'individual' is supported
  name: recipient_type
  type: string
- description: Recipient phone number in E.164 format without the leading +
  name: to
  type: string
- description: Message type
  name: type
  type: string
- description: ''
  name: context
  type: object
- description: Arbitrary string for tracking, included in webhook delivery
  name: biz_opaque_callback_data
  type: string
- description: ''
  name: text
  type: object
- description: ''
  name: image
  type: object
- description: ''
  name: video
  type: object
- description: ''
  name: audio
  type: object
- description: ''
  name: document
  type: object
- description: ''
  name: sticker
  type: object
- description: ''
  name: location
  type: object
- description: Array of contact cards to send
  name: contacts
  type: array
- description: ''
  name: interactive
  type: object
- description: ''
  name: template
  type: object
- description: ''
  name: reaction
  type: object
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-message-schema.json
slug: whatsapp-message
tags: []
title: WhatsApp Message
---
