---
description: ''
layout: schema
name: ChatCompletionRequest
properties_list:
- description: The model identifier, e.g. @cf/meta/llama-3.1-8b-instruct.
  name: model
  type: string
- description: ''
  name: messages
  type: array
- description: Maximum number of tokens to generate.
  name: max_tokens
  type: integer
- description: Sampling temperature between 0 and 2.
  name: temperature
  type: number
- description: Nucleus sampling parameter.
  name: top_p
  type: number
- description: Whether to stream the response via server-sent events.
  name: stream
  type: boolean
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-workers-ai-chat-completion-request-schema.json
slug: cloudflare-workers-ai-chat-completion-request
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
title: ChatCompletionRequest
---
