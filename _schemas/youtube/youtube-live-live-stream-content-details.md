---
description: Detailed settings for a live stream including the stream key and ingestion settings.
layout: schema
name: LiveStreamContentDetails
properties_list:
- description: The ID of the live broadcast to which this stream is bound.
  name: boundBroadcastId
  type: string
- description: Indicates whether the stream is reusable, which means that it can be bound to multiple broadcasts.
  name: isReusable
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-stream-content-details-schema.json
slug: youtube-live-live-stream-content-details
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveStreamContentDetails
---
