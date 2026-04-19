---
description: ''
layout: schema
name: ResponseInputContentPart
properties_list:
- description: The type of the content part.
  name: type
  type: string
- description: The text content. Used when type is input_text.
  name: text
  type: string
- description: The URL of the image. Used when type is input_image.
  name: image_url
  type: string
- description: The detail level for image inputs.
  name: detail
  type: string
- description: The ID of the uploaded file. Used when type is input_file.
  name: file_id
  type: string
- description: The name of the file.
  name: filename
  type: string
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-response-input-content-part-schema.json
slug: chatgpt-responses-response-input-content-part
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
title: ResponseInputContentPart
---
