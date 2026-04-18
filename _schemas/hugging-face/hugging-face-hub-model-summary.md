---
description: ''
layout: schema
name: ModelSummary
properties_list:
- description: Unique model identifier
  name: _id
  type: string
- description: Model repository ID (e.g., bert-base-uncased)
  name: id
  type: string
- description: Alias for id
  name: modelId
  type: string
- description: Model author or organization
  name: author
  type: string
- description: Latest commit SHA
  name: sha
  type: string
- description: Last modification timestamp
  name: lastModified
  type: string
- description: Whether the model is private
  name: private
  type: boolean
- description: ''
  name: disabled
  type: boolean
- description: Whether access is gated
  name: gated
  type: boolean
- description: Pipeline task tag
  name: pipeline_tag
  type: string
- description: ''
  name: tags
  type: array
- description: Total download count
  name: downloads
  type: integer
- description: Total like count
  name: likes
  type: integer
- description: Primary ML library
  name: library_name
  type: string
- description: ''
  name: createdAt
  type: string
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-hub-model-summary-schema.json
slug: hugging-face-hub-model-summary
tags: []
title: ModelSummary
---
