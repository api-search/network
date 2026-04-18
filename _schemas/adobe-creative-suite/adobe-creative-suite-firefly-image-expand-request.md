---
description: Request body for generative image expansion
layout: schema
name: ImageExpandRequest
properties_list:
- description: Text prompt to guide what content fills the expanded areas
  name: prompt
  type: string
- description: Text describing what to avoid in the expanded areas
  name: negativePrompt
  type: string
- description: ''
  name: image
  type: object
- description: ''
  name: size
  type: object
- description: Placement and inset parameters for the source image within the expanded canvas
  name: placement
  type: object
- description: ''
  name: numVariations
  type: integer
- description: ''
  name: seeds
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-image-expand-request-schema.json
slug: adobe-creative-suite-firefly-image-expand-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: ImageExpandRequest
---
