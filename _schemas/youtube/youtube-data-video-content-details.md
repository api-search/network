---
description: Information about the video content, including the length of the video and an indication of whether captions are available.
layout: schema
name: VideoContentDetails
properties_list:
- description: The length of the video in ISO 8601 format.
  name: duration
  type: string
- description: Indicates whether the video is available in 3D or in 2D.
  name: dimension
  type: string
- description: Indicates whether the video is available in high definition or standard definition.
  name: definition
  type: string
- description: Indicates whether captions are available for the video.
  name: caption
  type: string
- description: Indicates whether the video represents licensed content, which means that the content has been claimed by a YouTube content partner.
  name: licensedContent
  type: boolean
- description: Specifies the ratings that the video received under various rating schemes.
  name: contentRating
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-content-details-schema.json
slug: youtube-data-video-content-details
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoContentDetails
---
