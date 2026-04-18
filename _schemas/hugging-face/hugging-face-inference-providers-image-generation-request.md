---
description: ''
layout: schema
name: ImageGenerationRequest
properties_list:
- description: Image generation model ID
  name: model
  type: string
- description: Text prompt describing the image to generate
  name: prompt
  type: string
- description: Number of images to generate
  name: n
  type: integer
- description: Image dimensions
  name: size
  type: string
- description: ''
  name: response_format
  type: string
- description: Negative prompt to guide generation
  name: negative_prompt
  type: string
- description: Number of diffusion steps
  name: num_inference_steps
  type: integer
- description: Classifier-free guidance scale
  name: guidance_scale
  type: number
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-inference-providers-image-generation-request-schema.json
slug: hugging-face-inference-providers-image-generation-request
tags: []
title: ImageGenerationRequest
---
