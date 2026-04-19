---
description: A recorded video clip from a security camera.
layout: schema
name: VideoClip
properties_list:
- description: Unique identifier of the video clip.
  name: id
  type: string
- description: ID of the camera that recorded the clip.
  name: cameraId
  type: string
- description: Start timestamp of the recording.
  name: startTime
  type: string
- description: End timestamp of the recording.
  name: endTime
  type: string
- description: What triggered the recording.
  name: trigger
  type: string
- description: Pre-signed URL to download the video clip.
  name: downloadUrl
  type: string
- description: URL of the clip thumbnail image.
  name: thumbnailUrl
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-video-clip-schema.json
slug: platform-api-video-clip
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: VideoClip
---
