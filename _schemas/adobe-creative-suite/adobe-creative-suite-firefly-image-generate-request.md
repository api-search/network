---
description: Request body for text-to-image generation
layout: schema
name: ImageGenerateRequest
properties_list:
- description: Text description of the image to generate
  name: prompt
  type: string
- description: Text description of elements to avoid in the generated image
  name: negativePrompt
  type: string
- description: Broad content category to guide the generation model
  name: contentClass
  type: string
- description: Number of image variations to generate (1 to 4)
  name: numVariations
  type: integer
- description: ''
  name: size
  type: object
- description: ''
  name: style
  type: object
- description: Array of integer seed values for reproducible generation. Providing the same seed with the same prompt produces the same output.
  name: seeds
  type: array
- description: BCP 47 language locale for prompt interpretation
  name: locale
  type: string
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-image-generate-request-schema.json
slug: adobe-creative-suite-firefly-image-generate-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: ImageGenerateRequest
---
