---
description: Represents a communication channel for conversations.
layout: schema
name: Channel
properties_list:
- description: Unique identifier for the channel
  name: id
  type: string
- description: Display name of the channel
  name: name
  type: string
- description: Type of channel (e.g., EMAIL, CHAT, FACEBOOK)
  name: type
  type: string
- description: Associated account ID
  name: accountId
  type: string
- description: ISO 8601 timestamp when the channel was created
  name: createdAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-channel-schema.json
slug: conversations-api-channel
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
title: Channel
---
