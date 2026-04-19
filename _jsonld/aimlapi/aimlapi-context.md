---
class_count: 5
classes:
- ChatCompletionRequest
- ChatCompletionResponse
- ImageGenerationRequest
- EmbeddingRequest
- ModelInfo
context_file: json-ld/aimlapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/json-ld/aimlapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aimlapi from AIMLAPI.
layout: jsonld
name: Aimlapi Context
namespaces:
- prefix: aimlapi
  uri: https://aimlapi.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: model
  type: string
- container: set
  name: messages
  type: reference
- container: ''
  name: temperature
  type: decimal
- container: ''
  name: maxTokens
  type: integer
- container: ''
  name: stream
  type: boolean
- container: ''
  name: prompt
  type: string
- container: ''
  name: role
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: ownedBy
  type: string
- container: ''
  name: createdAt
  type: dateTime
property_count: 10
provider_name: AIMLAPI
provider_slug: aimlapi
slug: aimlapi-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
