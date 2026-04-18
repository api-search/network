---
description: ''
layout: schema
name: ChatCompletionRequest
properties_list:
- description: Model ID to use. Can be a Hugging Face model ID (e.g., meta-llama/Llama-3-70b-chat-hf) or a provider-specific identifier.
  name: model
  type: string
- description: List of messages comprising the conversation
  name: messages
  type: array
- description: Penalize tokens based on frequency in text so far
  name: frequency_penalty
  type: number
- description: Whether to return log probabilities
  name: logprobs
  type: boolean
- description: Maximum number of tokens to generate
  name: max_tokens
  type: integer
- description: Penalize tokens based on presence in text so far
  name: presence_penalty
  type: number
- description: Constrains effort on reasoning for models that support it. Common values are none, minimal, low, medium, high, xhigh.
  name: reasoning_effort
  type: string
- description: ''
  name: response_format
  type: string
- description: Random seed for reproducibility
  name: seed
  type: integer
- description: Up to 4 sequences where generation will stop
  name: stop
  type: array
- description: Whether to stream partial responses using SSE
  name: stream
  type: boolean
- description: ''
  name: stream_options
  type: object
- description: Sampling temperature
  name: temperature
  type: number
- description: Controls tool usage
  name: tool_choice
  type: string
- description: Prompt prepended before tools
  name: tool_prompt
  type: string
- description: List of tools the model may call
  name: tools
  type: array
- description: Number of most likely tokens to return per position
  name: top_logprobs
  type: integer
- description: Nucleus sampling parameter
  name: top_p
  type: number
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-providers-chat-completion-request-schema.json
slug: hugging-face-inference-providers-chat-completion-request
tags: []
title: ChatCompletionRequest
---
