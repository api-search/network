---
description: ''
layout: schema
name: ChatCompletionRequest
properties_list:
- description: Model identifier (can be tgi or a model ID)
  name: model
  type: string
- description: Conversation messages
  name: messages
  type: array
- description: ''
  name: frequency_penalty
  type: number
- description: ''
  name: logprobs
  type: boolean
- description: Maximum tokens to generate
  name: max_tokens
  type: integer
- description: ''
  name: presence_penalty
  type: number
- description: ''
  name: response_format
  type: string
- description: ''
  name: seed
  type: integer
- description: ''
  name: stop
  type: array
- description: ''
  name: stream
  type: boolean
- description: ''
  name: stream_options
  type: object
- description: ''
  name: temperature
  type: number
- description: ''
  name: tool_choice
  type: string
- description: Prompt appended before tools
  name: tool_prompt
  type: string
- description: ''
  name: tools
  type: array
- description: ''
  name: top_logprobs
  type: integer
- description: ''
  name: top_p
  type: number
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-text-generation-inference-chat-completion-request-schema.json
slug: hugging-face-text-generation-inference-chat-completion-request
tags: []
title: ChatCompletionRequest
---
