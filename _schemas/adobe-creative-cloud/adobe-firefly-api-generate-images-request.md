---
description: GenerateImagesRequest from Adobe API
layout: schema
name: GenerateImagesRequest
properties_list:
- description: Text description of the image to generate.
  name: prompt
  type: string
- description: Text describing elements to exclude from generation.
  name: negativePrompt
  type: string
- description: Number of image variations to generate.
  name: numVariations
  type: integer
- description: Output image dimensions.
  name: size
  type: object
- description: Content class hint. photo optimizes for photorealistic output, art for artistic/illustrated styles.
  name: contentClass
  type: string
- description: Style configuration for generation.
  name: style
  type: object
- description: Random seeds for reproducible generation. One seed per requested variation.
  name: seeds
  type: array
provider_name: Adobe Creative Cloud
provider_slug: adobe-creative-cloud
schema_file: json-schema/adobe-firefly-api-generate-images-request-schema.json
slug: adobe-firefly-api-generate-images-request
tags:
- AI/ML
- Cloud
- Creative
- Design
- Documents
- Photography
- SaaS
- Video
title: GenerateImagesRequest
---
