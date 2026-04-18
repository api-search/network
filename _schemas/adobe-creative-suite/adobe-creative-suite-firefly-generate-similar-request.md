---
description: Request body for generating images similar to a reference image
layout: schema
name: GenerateSimilarRequest
properties_list:
- description: Optional text prompt to further guide the style or content
  name: prompt
  type: string
- description: ''
  name: image
  type: object
- description: ''
  name: numVariations
  type: integer
- description: ''
  name: size
  type: object
- description: ''
  name: seeds
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-generate-similar-request-schema.json
slug: adobe-creative-suite-firefly-generate-similar-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: GenerateSimilarRequest
---
