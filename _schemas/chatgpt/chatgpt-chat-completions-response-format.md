---
description: An object specifying the format that the model must output. Setting to json_schema enables Structured Outputs which ensures the model will match your supplied JSON schema.
layout: schema
name: ResponseFormat
properties_list:
- description: The type of response format.
  name: type
  type: string
- description: The JSON schema the model must conform to. Required when type is json_schema.
  name: json_schema
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-response-format-schema.json
slug: chatgpt-chat-completions-response-format
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
title: ResponseFormat
---
