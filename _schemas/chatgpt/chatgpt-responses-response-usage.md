---
description: ''
layout: schema
name: ResponseUsage
properties_list:
- description: The number of input tokens used.
  name: input_tokens
  type: integer
- description: A detailed breakdown of input token usage.
  name: input_tokens_details
  type: object
- description: The number of output tokens generated.
  name: output_tokens
  type: integer
- description: A detailed breakdown of output token usage.
  name: output_tokens_details
  type: object
- description: The total number of tokens used.
  name: total_tokens
  type: integer
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-response-usage-schema.json
slug: chatgpt-responses-response-usage
tags:
- Agents
- AI
- ChatGPT
- Embeddings
- Fine-Tuning
- GPT-4
- GPT-5
- Language Model
- OpenAI
- Realtime
title: ResponseUsage
---
