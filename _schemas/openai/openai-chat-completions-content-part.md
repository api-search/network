---
description: ''
layout: schema
name: ContentPart
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
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-chat-completions-content-part-schema.json
slug: openai-chat-completions-content-part
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: ContentPart
---
