---
aid: openai:openai-embeddings-api
name: OpenAI Embeddings API
tags:
  - Creates
  - Embedding
  - Embeddings
  - Inputs
  - Representing
  - Text
  - Vectors
score: 112
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/guides/embeddings
overlays:
  - url: >-
      overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/embeddings-openapi-search.yml
    type: APIs.io Search
  - url: overlays/embeddings-openapi-search.yml
    type: APIs.io Search
  - url: overlays/embeddings-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/guides/embeddings
    type: Documentation
  - url: properties/embeddings-openapi-original.yml
    type: OpenAPI
description: >-
  Learn how to turn text into numbers, unlocking use cases like search. OpenAI's
  text embeddings measure the relatedness of text strings.

---