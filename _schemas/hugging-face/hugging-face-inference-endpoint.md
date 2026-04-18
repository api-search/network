---
description: Schema for a dedicated Inference Endpoint deployment on the Hugging Face platform, including model configuration, compute resources, scaling settings, and runtime status.
layout: schema
name: Hugging Face Inference Endpoint
properties_list:
- description: Unique name of the Inference Endpoint
  name: name
  type: string
- description: Account or organization ID that owns the endpoint
  name: accountId
  type: string
- description: Security type controlling endpoint access
  name: type
  type: string
- description: Cloud provider configuration
  name: provider
  type: object
- description: Compute resources configuration
  name: compute
  type: object
- description: Model deployment configuration
  name: model
  type: object
- description: Current status of the endpoint
  name: status
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-endpoint-schema.json
slug: hugging-face-inference-endpoint
tags: []
title: Hugging Face Inference Endpoint
---
