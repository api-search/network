---
description: Request body for generating an image via AIMLAPI
layout: schema
name: ImageGenerationRequest
properties_list:
- description: Image generation model ID
  name: model
  type: string
- description: Text description of desired image
  name: prompt
  type: string
- description: Number of images to generate
  name: n
  type: integer
- description: Image dimensions
  name: size
  type: string
- description: Image quality (standard, hd)
  name: quality
  type: string
- description: Image style (vivid, natural)
  name: style
  type: string
provider_name: AIMLAPI
provider_slug: aimlapi
schema_file: json-schema/aimlapi-image-generation-request-schema.json
slug: aimlapi-image-generation-request
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
title: ImageGenerationRequest
---
