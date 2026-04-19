---
description: ''
layout: schema
name: CreateMessageRequest
properties_list:
- description: The model that will complete your prompt. See the list of available models.
  name: model
  type: string
- description: The maximum number of tokens to generate before stopping. Different models support different maximum values.
  name: max_tokens
  type: integer
- description: Input messages. Alternating user and assistant conversational turns. Maximum 100,000 messages per request.
  name: messages
  type: array
- description: System prompt providing context and instructions to Claude. Can be a string or array of content blocks.
  name: system
  type: string
- description: Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Use closer to 0.0 for analytical tasks, closer to 1.0 for creative tasks.
  name: temperature
  type: number
- description: Use nucleus sampling. Recommended to use either temperature or top_p, but not both.
  name: top_p
  type: number
- description: Only sample from the top K options for each subsequent token.
  name: top_k
  type: integer
- description: Custom text sequences that will cause the model to stop generating.
  name: stop_sequences
  type: array
- description: Whether to incrementally stream the response using server-sent events.
  name: stream
  type: boolean
- description: Definitions of tools that the model may use.
  name: tools
  type: array
- description: Service tier to use for this request.
  name: service_tier
  type: string
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-create-message-request-schema.json
slug: claude-messages-create-message-request
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: CreateMessageRequest
---
