---
description: ''
layout: schema
name: StreamResponse
properties_list:
- description: ''
  name: token
  type: object
- description: Full generated text (only in the last event)
  name: generated_text
  type: string
- description: Generation details (only in the last event)
  name: details
  type: object
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-text-generation-inference-stream-response-schema.json
slug: hugging-face-text-generation-inference-stream-response
tags: []
title: StreamResponse
---
