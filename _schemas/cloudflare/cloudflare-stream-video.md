---
description: ''
layout: schema
name: Video
properties_list:
- description: The unique identifier of the video.
  name: uid
  type: string
- description: URL of the video thumbnail.
  name: thumbnail
  type: string
- description: ''
  name: playback
  type: object
- description: ''
  name: status
  type: object
- description: User-defined metadata.
  name: meta
  type: object
- description: ''
  name: created
  type: string
- description: ''
  name: modified
  type: string
- description: Duration of the video in seconds.
  name: duration
  type: number
- description: Size of the video in bytes.
  name: size
  type: integer
- description: ''
  name: requireSignedURLs
  type: boolean
- description: ''
  name: allowedOrigins
  type: array
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-stream-video-schema.json
slug: cloudflare-stream-video
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
title: Video
---
