---
description: ''
layout: schema
name: CompletionUsage
properties_list:
- description: Number of tokens in the prompt.
  name: prompt_tokens
  type: integer
- description: Number of tokens in the generated completion.
  name: completion_tokens
  type: integer
- description: Total number of tokens used in the request.
  name: total_tokens
  type: integer
- description: Breakdown of tokens used in a completion.
  name: completion_tokens_details
  type: object
- description: Breakdown of tokens used in the prompt.
  name: prompt_tokens_details
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-completion-usage-schema.json
slug: chatgpt-chat-completions-completion-usage
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
title: CompletionUsage
---
