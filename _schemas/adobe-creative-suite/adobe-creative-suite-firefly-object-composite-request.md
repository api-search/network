---
description: Request body for generating an object composite in a scene
layout: schema
name: ObjectCompositeRequest
properties_list:
- description: Text description of the object to generate and composite
  name: prompt
  type: string
- description: Text describing what to avoid in the generated object
  name: negativePrompt
  type: string
- description: ''
  name: contentClass
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
schema_file: json-schema/adobe-creative-suite-firefly-object-composite-request-schema.json
slug: adobe-creative-suite-firefly-object-composite-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: ObjectCompositeRequest
---
