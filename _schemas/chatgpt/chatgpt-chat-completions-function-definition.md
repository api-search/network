---
description: ''
layout: schema
name: FunctionDefinition
properties_list:
- description: The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
  name: name
  type: string
- description: A description of what the function does, used by the model to choose when and how to call the function.
  name: description
  type: string
- description: The parameters the functions accepts, described as a JSON Schema object. Omitting parameters defines a function with an empty parameter list.
  name: parameters
  type: object
- description: Whether to enable strict schema adherence when generating the function call. When set to true, the model will always follow the exact schema defined in the parameters field.
  name: strict
  type: boolean
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-function-definition-schema.json
slug: chatgpt-chat-completions-function-definition
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
title: FunctionDefinition
---
