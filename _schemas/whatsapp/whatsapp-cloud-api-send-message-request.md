---
description: SendMessageRequest from WhatsApp API
layout: schema
name: SendMessageRequest
properties_list:
- description: ''
  name: messaging_product
  type: string
- description: ''
  name: recipient_type
  type: string
- description: Recipient phone number in E.164 format without the leading +
  name: to
  type: string
- description: ''
  name: type
  type: string
- description: Context for reply messages
  name: context
  type: object
- description: Arbitrary string for tracking, returned in webhooks
  name: biz_opaque_callback_data
  type: string
- description: Set to read to mark an incoming message as read
  name: status
  type: string
- description: ID of the message to mark as read (required when status is read)
  name: message_id
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
- description: ''
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
schema_file: json-schema/whatsapp-cloud-api-send-message-request-schema.json
slug: whatsapp-cloud-api-send-message-request
tags: []
title: SendMessageRequest
---
