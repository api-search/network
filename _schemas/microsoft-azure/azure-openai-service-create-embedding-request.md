---
description: Request body for creating embeddings.
layout: schema
name: CreateEmbeddingRequest
properties_list:
- description: Input text to embed, encoded as a string or array of strings.
  name: input
  type: string
- description: A unique identifier representing your end-user.
  name: user
  type: string
- description: The input type for the embedding request.
  name: input_type
  type: string
- description: The format to return the embeddings in.
  name: encoding_format
  type: string
- description: The number of dimensions the resulting output embeddings should have.
  name: dimensions
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-embedding-request-schema.json
slug: azure-openai-service-create-embedding-request
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateEmbeddingRequest
---
