---
description: ''
layout: schema
name: SubscriptionRequest
properties_list:
- description: The type of change to subscribe to.
  name: changeType
  type: string
- description: The URL to receive change notifications.
  name: notificationUrl
  type: string
- description: The resource path to subscribe to. For Copilot interactions use /copilot/interactionHistory/getAllEnterpriseInteractions.
  name: resource
  type: string
- description: The date and time when the subscription expires.
  name: expirationDateTime
  type: string
- description: Optional client state value included in each notification for validation.
  name: clientState
  type: string
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-subscription-request-schema.json
slug: microsoft-copilot-subscription-request
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
title: SubscriptionRequest
---
