---
description: ''
layout: schema
name: ResponseOutputItem
properties_list:
- description: The type of the output item.
  name: type
  type: string
- description: The unique ID of the output item.
  name: id
  type: string
- description: The role of the output item.
  name: role
  type: string
- description: The status of the output item.
  name: status
  type: string
- description: The content of the output message. Present when type is message.
  name: content
  type: array
- description: The name of the function being called. Present when type is function_call.
  name: name
  type: string
- description: The unique ID of the function call. Present when type is function_call.
  name: call_id
  type: string
- description: The arguments to the function call in JSON format. Present when type is function_call.
  name: arguments
  type: string
- description: A summary of the reasoning performed by the model. Present when type is reasoning.
  name: summary
  type: array
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-response-output-item-schema.json
slug: chatgpt-responses-response-output-item
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
title: ResponseOutputItem
---
