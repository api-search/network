---
description: Schema representing an Amazon Bedrock foundation model and its capabilities.
layout: schema
name: Amazon Bedrock Foundation Model
properties_list:
- description: The Amazon Resource Name (ARN) of the foundation model.
  name: modelArn
  type: string
- description: The unique identifier for the foundation model (e.g., anthropic.claude-3-sonnet-20240229-v1:0).
  name: modelId
  type: string
- description: The display name of the foundation model.
  name: modelName
  type: string
- description: The name of the model provider.
  name: providerName
  type: string
- description: The input modalities supported by the model.
  name: inputModalities
  type: array
- description: The output modalities supported by the model.
  name: outputModalities
  type: array
- description: Whether the model supports response streaming.
  name: responseStreamingSupported
  type: boolean
- description: The customization types supported by the model.
  name: customizationsSupported
  type: array
- description: The inference types supported by the model.
  name: inferenceTypesSupported
  type: array
- description: Lifecycle information for the model.
  name: modelLifecycle
  type: object
provider_name: Amazon Bedrock
provider_slug: amazon-bedrock
schema_file: json-schema/amazon-bedrock-model-schema.json
slug: amazon-bedrock-model
tags:
- AI
- AWS
- Foundation Models
- Generative AI
- LLM
- Machine Learning
- RAG
- Agents
- Responsible AI
title: Amazon Bedrock Foundation Model
---
