---
description: ''
layout: schema
name: CompletionRequest
properties_list:
- description: Model ID to use
  name: model
  type: string
- description: Prompt(s) to generate completions for
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
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-providers-completion-request-schema.json
slug: hugging-face-inference-providers-completion-request
tags: []
title: CompletionRequest
---
