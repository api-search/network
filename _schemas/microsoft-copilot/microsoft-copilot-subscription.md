---
description: ''
layout: schema
name: Subscription
properties_list:
- description: The unique identifier of the subscription.
  name: id
  type: string
- description: The resource being monitored.
  name: resource
  type: string
- description: The type of change being monitored.
  name: changeType
  type: string
- description: The URL receiving notifications.
  name: notificationUrl
  type: string
- description: When the subscription expires.
  name: expirationDateTime
  type: string
- description: The client state value for validation.
  name: clientState
  type: string
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-subscription-schema.json
slug: microsoft-copilot-subscription
tags:
- Agents
- AI Assistant
- Artificial Intelligence
- Chatbot
- Copilot
- Extensibility
- Generative AI
- Microsoft 365
- Productivity
title: Subscription
---
