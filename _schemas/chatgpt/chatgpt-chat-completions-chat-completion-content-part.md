---
description: ''
layout: schema
name: ChatCompletionContentPart
properties_list:
- description: The type of the content part.
  name: type
  type: string
- description: The text content. Required when type is text.
  name: text
  type: string
- description: The image URL content. Required when type is image_url.
  name: image_url
  type: object
- description: The audio content. Required when type is input_audio.
  name: input_audio
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-chat-completion-content-part-schema.json
slug: chatgpt-chat-completions-chat-completion-content-part
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
title: ChatCompletionContentPart
---
