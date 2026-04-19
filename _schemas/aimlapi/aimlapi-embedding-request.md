---
description: Request body for creating text embeddings via AIMLAPI
layout: schema
name: EmbeddingRequest
properties_list:
- description: Embedding model ID
  name: model
  type: string
- description: Text to embed
  name: input
  type: string
- description: Encoding format (float, base64)
  name: encoding_format
  type: string
- description: Output embedding dimensions
  name: dimensions
  type: integer
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-embedding-request-schema.json
slug: aimlapi-embedding-request
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
title: EmbeddingRequest
---
