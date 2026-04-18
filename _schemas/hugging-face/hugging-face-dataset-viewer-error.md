---
description: ''
layout: schema
name: Error
properties_list:
- description: Error message
  name: error
  type: string
- description: Underlying exception type
  name: cause_exception
  type: string
- description: Underlying exception message
  name: cause_message
  type: string
- description: Stack trace (only in development)
  name: cause_traceback
  type: array
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-dataset-viewer-error-schema.json
slug: hugging-face-dataset-viewer-error
tags: []
title: Error
---
