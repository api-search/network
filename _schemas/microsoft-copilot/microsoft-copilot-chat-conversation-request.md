---
description: ''
layout: schema
name: ChatConversationRequest
properties_list:
- description: Natural language prompt to send to Microsoft 365 Copilot to start a conversation.
  name: prompt
  type: string
- description: Whether to enable web search grounding for this message. Defaults to true. Must be toggled off per message if not desired.
  name: enableWebSearch
  type: boolean
- description: Optional OneDrive and SharePoint file references to provide as additional context.
  name: fileReferences
  type: array
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-chat-conversation-request-schema.json
slug: microsoft-copilot-chat-conversation-request
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
title: ChatConversationRequest
---
