---
description: ''
layout: schema
name: TokenLogprob
properties_list:
- description: The token.
  name: token
  type: string
- description: The log probability of this token.
  name: logprob
  type: number
- description: A list of integers representing the UTF-8 bytes representation of the token.
  name: bytes
  type: array
- description: List of the most likely tokens and their log probability.
  name: top_logprobs
  type: array
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-token-logprob-schema.json
slug: chatgpt-chat-completions-token-logprob
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
title: TokenLogprob
---
