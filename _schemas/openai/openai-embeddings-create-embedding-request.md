---
description: ''
layout: schema
name: CreateEmbeddingRequest
properties_list:
- description: ID of the model to use. You can use the List Models API to see all available models, or see the Model overview for descriptions.
  name: model
  type: string
- description: Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input to
  name: input
  type: string
- description: The format to return the embeddings in. Can be either float or base64. Defaults to float.
  name: encoding_format
  type: string
- description: The number of dimensions the resulting output embeddings should have. Only supported in text-embedding-3 and later models.
  name: dimensions
  type: integer
- description: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  name: user
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-embeddings-create-embedding-request-schema.json
slug: openai-embeddings-create-embedding-request
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateEmbeddingRequest
---
