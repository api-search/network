---
description: ''
layout: schema
name: ChatCompletionChoice
properties_list:
- description: The index of the choice in the list.
  name: index
  type: integer
- description: 'The reason the model stopped generating tokens. stop means the model hit a natural stop point or a provided stop sequence. length means the maximum token limit was reached. tool_calls means the model '
  name: finish_reason
  type: string
- description: Log probability information for the choice.
  name: logprobs
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-chat-completion-choice-schema.json
slug: chatgpt-chat-completions-chat-completion-choice
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
title: ChatCompletionChoice
---
