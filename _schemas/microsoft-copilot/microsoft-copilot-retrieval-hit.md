---
description: ''
layout: schema
name: RetrievalHit
properties_list:
- description: The URL of the source document.
  name: webUrl
  type: string
- description: Collection of relevant text extracts from the document.
  name: extracts
  type: array
- description: The type of resource. Values include listItem (for SharePoint/OneDrive) and externalItem (for Copilot connectors).
  name: resourceType
  type: string
- description: Metadata fields for the resource, as requested via the resourceMetadata parameter. Keys and values depend on the requested fields.
  name: resourceMetadata
  type: object
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-retrieval-hit-schema.json
slug: microsoft-copilot-retrieval-hit
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
title: RetrievalHit
---
