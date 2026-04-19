---
description: A chat completion response object returned by the OpenAI Chat Completions API. Represents a model-generated message in response to a conversation comprising a list of messages.
layout: schema
name: OpenAI Chat Completion
properties_list:
- description: A unique identifier for the chat completion. Prefixed with chatcmpl-.
  name: id
  type: string
- description: The object type, which is always chat.completion.
  name: object
  type: string
- description: The Unix timestamp (in seconds) of when the chat completion was created.
  name: created
  type: integer
- description: The model used for the chat completion (e.g., gpt-5, gpt-4.1, o4-mini).
  name: model
  type: string
- description: 'This fingerprint represents the backend configuration that the model runs with. Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might '
  name: system_fingerprint
  type:
  - string
  - 'null'
- description: The service tier used for processing the request. This field is only included if the service_tier parameter is specified in the request.
  name: service_tier
  type:
  - string
  - 'null'
- description: A list of chat completion choices. Can be more than one if n is greater than 1.
  name: choices
  type: array
- description: ''
  name: usage
  type: object
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-chat-completion-schema.json
slug: openai-chat-completion
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: OpenAI Chat Completion
---
