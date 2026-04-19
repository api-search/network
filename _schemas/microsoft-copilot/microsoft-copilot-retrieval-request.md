---
description: ''
layout: schema
name: RetrievalRequest
properties_list:
- description: Natural language query string used to retrieve relevant text extracts. Should be a single sentence. Avoid spelling errors in context-rich keywords.
  name: queryString
  type: string
- description: Indicates whether extracts should be retrieved from SharePoint, OneDrive, or Copilot connectors.
  name: dataSource
  type: string
- description: Keyword Query Language (KQL) expression with queryable properties to scope retrieval. Supports AND, OR, NOT, and inequality operators. Supported SharePoint/OneDrive properties include Author, FileExte
  name: filterExpression
  type: string
- description: List of metadata fields to return for each item. Only retrievable metadata properties can be included. By default, no metadata is returned.
  name: resourceMetadata
  type: array
- description: Number of results to return. Must be between 1 and 25. Defaults to 25.
  name: maximumNumberOfResults
  type: integer
provider_name: Microsoft Copilot
provider_slug: microsoft-copilot
schema_file: json-schema/microsoft-copilot-retrieval-request-schema.json
slug: microsoft-copilot-retrieval-request
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
title: RetrievalRequest
---
