---
description: Represents a message within a conversation thread.
layout: schema
name: Message
properties_list:
- description: Unique identifier for the message
  name: id
  type: string
- description: Type of message
  name: type
  type: string
- description: Plain text content of the message
  name: text
  type: string
- description: Rich text (HTML) content of the message
  name: richText
  type: string
- description: Direction of the message (incoming or outgoing)
  name: direction
  type: string
- description: ID of the communication channel
  name: channelId
  type: string
- description: ID of the channel account
  name: channelAccountId
  type: string
- description: List of message senders
  name: senders
  type: array
- description: List of message recipients
  name: recipients
  type: array
- description: Delivery status information for a message
  name: status
  type: object
- description: ISO 8601 timestamp when the message was created
  name: createdAt
  type: string
- description: Whether the message was truncated
  name: truncationStatus
  type: string
- description: Message attachments
  name: attachments
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-conversations-message-schema.json
slug: hubspot-conversations-message
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
title: Message
---
