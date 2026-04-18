---
description: ''
layout: schema
name: Image
properties_list:
- description: The unique identifier of the image.
  name: id
  type: string
- description: Original filename.
  name: filename
  type: string
- description: User-defined metadata.
  name: metadata
  type: object
- description: Upload timestamp.
  name: uploaded
  type: string
- description: ''
  name: requireSignedURLs
  type: boolean
- description: URLs for each variant of the image.
  name: variants
  type: array
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-images-image-schema.json
slug: cloudflare-images-image
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: Image
---
