---
description: Schema representing an interaction between a user and Microsoft 365 Copilot, including prompts, responses, attachments, contexts, links, and mentions. Based on the microsoft.graph.aiInteraction resource type from the Microsoft Graph Copilot namespace.
layout: schema
name: Microsoft 365 Copilot Interaction
properties_list:
- description: The unique identifier for the interaction message.
  name: id
  type: string
- description: The data source for Copilot data. Indicates which Microsoft 365 application hosted the interaction. Examples include IPM.SkypeTeams.Message.Copilot.Excel, IPM.SkypeTeams.Message.Copilot.Loop, IPM.Skyp
  name: appClass
  type: string
- description: The body of the message, including the text content and its body type.
  name: body
  type: object
- description: Indicates whether the interaction is a user prompt or a Copilot response. userPrompt represents a user's input; aiResponse represents Copilot's reply.
  name: interactionType
  type: string
- description: The type of the conversation. Common values include appchat (in-app Copilot interactions) and bizchat (Business Chat / Microsoft 365 Chat interactions).
  name: conversationType
  type: string
- description: The identifier that groups a user prompt with its corresponding Copilot response. Both the prompt and response in a single exchange share the same requestId.
  name: requestId
  type: string
- description: The thread ID or conversation identifier that maps to all Copilot sessions for the user. Groups all interactions within a single conversation session.
  name: sessionId
  type: string
- description: The ISO 8601 date and time when the interaction was created.
  name: createdDateTime
  type: string
- description: The timestamp of when the interaction was last modified. Used for concurrency control.
  name: etag
  type: string
- description: The locale of the sender, in BCP 47 language tag format.
  name: locale
  type: string
- description: The user, application, or device that is associated with this interaction.
  name: from
  type: object
- description: The collection of documents attached to the interaction, such as cards and images.
  name: attachments
  type: array
- description: The identifiers that map to all contexts associated with the interaction, such as the file or application in which the interaction occurred.
  name: contexts
  type: array
- description: The collection of links that appear in the interaction, including citation links and reference links.
  name: links
  type: array
- description: The collection of entities that were mentioned in the interaction, including users, bots, and other entities.
  name: mentions
  type: array
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-interaction-schema.json
slug: microsoft-copilot-interaction
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
title: Microsoft 365 Copilot Interaction
---
