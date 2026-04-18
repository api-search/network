---
description: Request body for creating image generations.
layout: schema
name: CreateImageRequest
properties_list:
- description: A text description of the desired image(s).
  name: prompt
  type: string
- description: The number of images to generate.
  name: n
  type: integer
- description: The size of the generated images.
  name: size
  type: string
- description: The quality of the image that will be generated.
  name: quality
  type: string
- description: The style of the generated images.
  name: style
  type: string
- description: The format in which the generated images are returned.
  name: response_format
  type: string
- description: A unique identifier representing your end-user.
  name: user
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-image-request-schema.json
slug: azure-openai-service-create-image-request
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateImageRequest
---
