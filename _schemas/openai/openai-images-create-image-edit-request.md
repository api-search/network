---
description: ''
layout: schema
name: CreateImageEditRequest
properties_list:
- description: The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, the image must have transparency which will be used as the mask.
  name: image
  type: string
- description: A text description of the desired image(s). The maximum length is 1000 characters for DALL-E 2 and 32000 characters for gpt-image-1.
  name: prompt
  type: string
- description: An additional image whose fully transparent areas indicate where the image should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as image.
  name: mask
  type: string
- description: The model to use for image editing.
  name: model
  type: string
- description: The number of images to generate.
  name: n
  type: integer
- description: The size of the generated images.
  name: size
  type: string
- description: The format in which the generated images are returned.
  name: response_format
  type: string
- description: A unique identifier representing your end-user.
  name: user
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-images-create-image-edit-request-schema.json
slug: openai-images-create-image-edit-request
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateImageEditRequest
---
