---
description: A liveStream resource contains information about the video stream that you are transmitting to YouTube. The stream provides the content that will be broadcast to YouTube users.
layout: schema
name: LiveStream
properties_list:
- description: Identifies the API resource's type. Value is youtube#liveStream.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube assigns to uniquely identify the stream.
  name: id
  type: string
- description: Basic details about a live stream including its title, description, and channel association.
  name: snippet
  type: object
- description: The cdn object defines the live stream's content delivery network (CDN) settings.
  name: cdn
  type: object
- description: Status information about a live stream including its stream status and health status.
  name: status
  type: object
- description: Detailed settings for a live stream including the stream key and ingestion settings.
  name: contentDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-stream-schema.json
slug: youtube-live-live-stream
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveStream
---
