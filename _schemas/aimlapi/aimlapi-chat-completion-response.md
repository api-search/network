---
description: Response from a chat completion request
layout: schema
name: ChatCompletionResponse
properties_list:
- description: Unique completion ID
  name: id
  type: string
- description: Object type
  name: object
  type: string
- description: Model used for completion
  name: model
  type: string
- description: List of completion choices
  name: choices
  type: array
- description: Token usage statistics
  name: usage
  type: object
- description: Unix timestamp of creation
  name: created
  type: integer
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-chat-completion-response-schema.json
slug: aimlapi-chat-completion-response
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
title: ChatCompletionResponse
---
