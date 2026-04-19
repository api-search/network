---
description: ''
layout: schema
name: LiveStreamUpdateRequest
properties_list:
- description: Streaming URL (e.g., RTMP endpoint).
  name: stream_url
  type: string
- description: Stream key or name.
  name: stream_key
  type: string
- description: The live stream page URL where viewers can watch.
  name: page_url
  type: string
- description: The live stream resolution. Can be 720p or 1080p.
  name: resolution
  type: string
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-live-stream-update-request-schema.json
slug: zoom-meeting-live-stream-update-request
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: LiveStreamUpdateRequest
---
