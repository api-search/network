---
description: Represents a conversation inbox configuration where messages are organized and routed.
layout: schema
name: Inbox
properties_list:
- description: Unique identifier for the inbox
  name: id
  type: string
- description: Display name of the inbox
  name: name
  type: string
- description: Type of inbox (e.g., CONVERSATIONS_INBOX)
  name: type
  type: string
- description: ISO 8601 timestamp when the inbox was created
  name: createdAt
  type: string
- description: ISO 8601 timestamp when the inbox was last updated
  name: updatedAt
  type: string
- description: Whether the inbox is archived
  name: archived
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-inbox-schema.json
slug: conversations-api-inbox
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
title: Inbox
---
