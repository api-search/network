---
description: A response object returned by the OpenAI Embeddings API. Contains a list of embedding vectors representing the input text as floating-point numbers, along with the model used and token usage statistics.
layout: schema
name: OpenAI Embedding Response
properties_list:
- description: The object type, which is always list.
  name: object
  type: string
- description: The list of embedding objects, one for each input.
  name: data
  type: array
- description: The name of the model used to generate the embeddings (e.g., text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002).
  name: model
  type: string
- description: ''
  name: usage
  type: object
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-embedding-schema.json
slug: openai-embedding
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: OpenAI Embedding Response
---
