---
description: Request body for generative fill operation
layout: schema
name: ImageFillRequest
properties_list:
- description: Text prompt describing what to fill in the masked area
  name: prompt
  type: string
- description: Text describing what to avoid in the filled area
  name: negativePrompt
  type: string
- description: ''
  name: image
  type: object
- description: ''
  name: mask
  type: object
- description: ''
  name: numVariations
  type: integer
- description: ''
  name: seeds
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-image-fill-request-schema.json
slug: adobe-creative-suite-firefly-image-fill-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: ImageFillRequest
---
