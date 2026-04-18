---
description: ''
layout: schema
name: QuestionAnsweringResponse
properties_list:
- description: The extracted answer
  name: answer
  type: string
- description: Confidence score
  name: score
  type: number
- description: Start character position in context
  name: start
  type: integer
- description: End character position in context
  name: end
  type: integer
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-question-answering-response-schema.json
slug: hugging-face-inference-question-answering-response
tags: []
title: QuestionAnsweringResponse
---
