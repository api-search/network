---
description: ''
layout: schema
name: FillMaskResponse
properties_list:
- description: The complete text with filled mask
  name: sequence
  type: string
- description: Confidence score for the prediction
  name: score
  type: number
- description: Token ID of the predicted word
  name: token
  type: integer
- description: The predicted word
  name: token_str
  type: string
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-fill-mask-response-schema.json
slug: hugging-face-inference-fill-mask-response
tags: []
title: FillMaskResponse
---
