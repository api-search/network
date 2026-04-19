---
description: ''
layout: schema
name: RetrievalExtract
properties_list:
- description: The relevant text extract from the document.
  name: text
  type: string
- description: Cosine similarity between the queryString and the extract, normalized to the 0-1 range. May be absent for Copilot connectors results.
  name: relevanceScore
  type: number
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-retrieval-extract-schema.json
slug: microsoft-copilot-retrieval-extract
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
title: RetrievalExtract
---
