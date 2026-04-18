---
description: Represents a conversation thread containing messages between participants.
layout: schema
name: Thread
properties_list:
- description: Unique identifier for the thread
  name: id
  type: string
- description: ID of the inbox containing this thread
  name: inboxId
  type: string
- description: Current status of the thread
  name: status
  type: string
- description: Whether the thread is marked as spam
  name: spam
  type: boolean
- description: ID of the associated CRM contact
  name: associatedContactId
  type: string
- description: User ID the thread is assigned to
  name: assignedTo
  type: string
- description: ID of the original communication channel
  name: originalChannelId
  type: string
- description: ID of the original channel account
  name: originalChannelAccountId
  type: string
- description: ISO 8601 timestamp of the latest message
  name: latestMessageTimestamp
  type: string
- description: ISO 8601 timestamp of the latest sent message
  name: latestMessageSentTimestamp
  type: string
- description: ISO 8601 timestamp of the latest received message
  name: latestMessageReceivedTimestamp
  type: string
- description: ISO 8601 timestamp when the thread was closed
  name: closedAt
  type: string
- description: ISO 8601 timestamp when the thread was created
  name: createdAt
  type: string
- description: Whether the thread is archived
  name: archived
  type: boolean
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/conversations-api-thread-schema.json
slug: conversations-api-thread
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
title: Thread
---
