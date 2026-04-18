---
description: ''
layout: schema
name: Info
properties_list:
- description: Loaded model ID
  name: model_id
  type: string
- description: Model revision SHA
  name: model_sha
  type: string
- description: Model data type
  name: model_dtype
  type: string
- description: Device type (cuda, cpu)
  name: model_device_type
  type: string
- description: Pipeline task tag
  name: model_pipeline_tag
  type: string
- description: ''
  name: max_concurrent_requests
  type: integer
- description: ''
  name: max_best_of
  type: integer
- description: ''
  name: max_stop_sequences
  type: integer
- description: Maximum input token length
  name: max_input_length
  type: integer
- description: Maximum total tokens (input + output)
  name: max_total_tokens
  type: integer
- description: ''
  name: waiting_served_ratio
  type: number
- description: ''
  name: max_batch_total_tokens
  type: integer
- description: ''
  name: max_waiting_tokens
  type: integer
- description: ''
  name: validation_workers
  type: integer
- description: ''
  name: max_client_batch_size
  type: integer
- description: TGI version
  name: version
  type: string
- description: TGI build SHA
  name: sha
  type: string
- description: Docker image label
  name: docker_label
  type: string
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-text-generation-inference-info-schema.json
slug: hugging-face-text-generation-inference-info
tags: []
title: Info
---
