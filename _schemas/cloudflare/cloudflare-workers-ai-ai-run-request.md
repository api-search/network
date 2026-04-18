---
description: ''
layout: schema
name: AiRunRequest
properties_list:
- description: The input prompt for text generation models.
  name: prompt
  type: string
- description: Array of messages for chat-style models.
  name: messages
  type: array
- description: Raw image bytes for image classification models.
  name: image
  type: array
- description: Text input for embedding or translation models.
  name: text
  type: string
- description: Source language code for translation.
  name: source_lang
  type: string
- description: Target language code for translation.
  name: target_lang
  type: string
- description: Maximum number of tokens to generate.
  name: max_tokens
  type: integer
- description: Sampling temperature.
  name: temperature
  type: number
- description: Whether to stream the response using server-sent events.
  name: stream
  type: boolean
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-workers-ai-ai-run-request-schema.json
slug: cloudflare-workers-ai-ai-run-request
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: AiRunRequest
---
