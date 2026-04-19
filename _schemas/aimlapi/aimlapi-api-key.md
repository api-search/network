---
description: An AIMLAPI API key for authentication
layout: schema
name: ApiKey
properties_list:
- description: API key identifier
  name: id
  type: string
- description: Human-readable key name
  name: name
  type: string
- description: The API key value (only shown on creation)
  name: key
  type: string
- description: Creation timestamp
  name: created_at
  type: string
- description: 'Key status: active, disabled'
  name: status
  type: string
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-api-key-schema.json
slug: aimlapi-api-key
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
title: ApiKey
---
