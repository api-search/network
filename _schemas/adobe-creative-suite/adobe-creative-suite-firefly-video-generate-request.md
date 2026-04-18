---
description: Request body for text-to-video generation
layout: schema
name: VideoGenerateRequest
properties_list:
- description: Text description of the video to generate
  name: prompt
  type: string
- description: Text describing what to avoid in the generated video
  name: negativePrompt
  type: string
- description: Output video dimensions
  name: size
  type: object
- description: Requested video duration in seconds
  name: duration
  type: number
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-video-generate-request-schema.json
slug: adobe-creative-suite-firefly-video-generate-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: VideoGenerateRequest
---
