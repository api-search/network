---
description: ''
layout: schema
name: CreateImageRequest
properties_list:
- description: A text description of the desired image(s). The maximum length is 1000 characters for DALL-E 2 and 32000 characters for gpt-image-1.
  name: prompt
  type: string
- description: The model to use for image generation. Defaults to dall-e-2.
  name: model
  type: string
- description: The number of images to generate. Must be between 1 and 10. For DALL-E 3, only n=1 is supported.
  name: n
  type: integer
- description: The quality of the image. hd creates images with finer details and greater consistency. For gpt-image-1 use low, medium, high, or auto.
  name: quality
  type: string
- description: The format in which the generated images are returned. Must be one of url or b64_json. URLs are only valid for 60 minutes.
  name: response_format
  type: string
- description: The size of the generated images. Must be one of the supported sizes for the model being used.
  name: size
  type: string
- description: The style of the generated images. Vivid generates hyper-real and dramatic images. Natural produces more natural, less hyper-real images. Only supported for DALL-E 3.
  name: style
  type: string
- description: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  name: user
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-images-create-image-request-schema.json
slug: openai-images-create-image-request
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateImageRequest
---
