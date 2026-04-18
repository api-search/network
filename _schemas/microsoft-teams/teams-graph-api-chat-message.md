---
description: Represents a message in a channel or chat.
layout: schema
name: ChatMessage
properties_list:
- description: Unique identifier for the message.
  name: id
  type: string
- description: When the message was created.
  name: createdDateTime
  type: string
- description: When the message was last modified.
  name: lastModifiedDateTime
  type: string
- description: The type of message.
  name: messageType
  type: string
- description: Message importance.
  name: importance
  type: string
- description: Subject of the message.
  name: subject
  type: string
- description: Message body content.
  name: body
  type: object
- description: Sender information.
  name: from
  type: object
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-chat-message-schema.json
slug: teams-graph-api-chat-message
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: ChatMessage
---
