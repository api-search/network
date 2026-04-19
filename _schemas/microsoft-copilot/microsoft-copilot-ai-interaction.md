---
description: Represents an interaction between a user and Copilot across Microsoft 365 applications.
layout: schema
name: AiInteraction
properties_list:
- description: The unique identifier for the interaction message.
  name: id
  type: string
- description: The data source for Copilot data. For example, IPM.SkypeTeams.Message.Copilot.Excel or IPM.SkypeTeams.Message.Copilot.Loop.
  name: appClass
  type: string
- description: Indicates whether the interaction is a user prompt or a Copilot response.
  name: interactionType
  type: string
- description: The type of the conversation (e.g., appchat, bizchat).
  name: conversationType
  type: string
- description: Identifier that groups a user prompt with its corresponding Copilot response.
  name: requestId
  type: string
- description: Thread ID or conversation identifier that maps to all Copilot sessions for the user.
  name: sessionId
  type: string
- description: The time when the interaction was created.
  name: createdDateTime
  type: string
- description: Timestamp of when the interaction was last modified.
  name: etag
  type: string
- description: The locale of the sender.
  name: locale
  type: string
- description: Collection of documents attached to the interaction, such as cards and images.
  name: attachments
  type: array
- description: Identifiers that map to all contexts associated with the interaction.
  name: contexts
  type: array
- description: Collection of links that appear in the interaction.
  name: links
  type: array
- description: Collection of entities mentioned in the interaction, including users and bots.
  name: mentions
  type: array
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-ai-interaction-schema.json
slug: microsoft-copilot-ai-interaction
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
title: AiInteraction
---
