---
description: ''
layout: schema
name: CompletionRequest
properties_list:
- description: ''
  name: model
  type: string
- description: ''
  name: prompt
  type: string
- description: ''
  name: max_tokens
  type: integer
- description: ''
  name: temperature
  type: number
- description: ''
  name: top_p
  type: number
- description: ''
  name: stop
  type: array
- description: ''
  name: stream
  type: boolean
- description: ''
  name: seed
  type: integer
- description: Suffix to append after generated text
  name: suffix
  type: string
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-text-generation-inference-completion-request-schema.json
slug: hugging-face-text-generation-inference-completion-request
tags: []
title: CompletionRequest
---
