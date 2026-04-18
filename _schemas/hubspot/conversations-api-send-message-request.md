---
description: Request payload for sending a message to a thread.
layout: schema
name: SendMessageRequest
properties_list:
- description: Type of message to send
  name: type
  type: string
- description: Plain text content of the message
  name: text
  type: string
- description: Rich text (HTML) content
  name: richText
  type: string
- description: Actor ID of the sender
  name: senderActorId
  type: string
- description: Channel to send on
  name: channelId
  type: string
- description: Channel account to use
  name: channelAccountId
  type: string
- description: Message recipients
  name: recipients
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-send-message-request-schema.json
slug: conversations-api-send-message-request
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: SendMessageRequest
---
