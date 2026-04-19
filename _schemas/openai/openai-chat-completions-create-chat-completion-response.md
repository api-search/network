---
description: ''
layout: schema
name: CreateChatCompletionResponse
properties_list:
- description: A unique identifier for the chat completion.
  name: id
  type: string
- description: The object type, always chat.completion.
  name: object
  type: string
- description: The Unix timestamp (in seconds) of when the completion was created.
  name: created
  type: integer
- description: The model used for the chat completion.
  name: model
  type: string
- description: A list of chat completion choices.
  name: choices
  type: array
- description: This fingerprint represents the backend configuration that the model runs with. Can be used with the seed parameter to detect backend changes.
  name: system_fingerprint
  type: string
- description: The service tier used for processing the request.
  name: service_tier
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-chat-completions-create-chat-completion-response-schema.json
slug: openai-chat-completions-create-chat-completion-response
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateChatCompletionResponse
---
