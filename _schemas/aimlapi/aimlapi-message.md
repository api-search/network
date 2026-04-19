---
description: A single message in a chat conversation
layout: schema
name: Message
properties_list:
- description: 'Message role: system, user, assistant, tool'
  name: role
  type: string
- description: Message content text
  name: content
  type: string
- description: Optional name for the participant
  name: name
  type: string
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-message-schema.json
slug: aimlapi-message
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
title: Message
---
