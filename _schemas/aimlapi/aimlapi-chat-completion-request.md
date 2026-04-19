---
description: Request body for creating a chat completion via AIMLAPI
layout: schema
name: ChatCompletionRequest
properties_list:
- description: Model ID to use for completion
  name: model
  type: string
- description: List of messages in the conversation
  name: messages
  type: array
- description: Sampling temperature 0-2
  name: temperature
  type: number
- description: Maximum tokens to generate
  name: max_tokens
  type: integer
- description: Stream response tokens
  name: stream
  type: boolean
- description: Nucleus sampling parameter
  name: top_p
  type: number
- description: Frequency penalty -2 to 2
  name: frequency_penalty
  type: number
- description: Presence penalty -2 to 2
  name: presence_penalty
  type: number
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-chat-completion-request-schema.json
slug: aimlapi-chat-completion-request
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
title: ChatCompletionRequest
---
