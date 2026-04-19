---
description: ''
layout: schema
name: Image
properties_list:
- description: The URL of the generated image, if response_format is url. The URL is valid for 60 minutes.
  name: url
  type: string
- description: The base64-encoded JSON of the generated image, if response_format is b64_json.
  name: b64_json
  type: string
- description: The prompt that was used to generate the image, if there was any revision to the prompt. Only present for DALL-E 3 and gpt-image-1.
  name: revised_prompt
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-images-image-schema.json
slug: openai-images-image
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: Image
---
