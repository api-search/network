---
description: A liveBroadcast resource represents an event that will be streamed, via live video, on YouTube.
layout: schema
name: LiveBroadcast
properties_list:
- description: Identifies the API resource's type. Value is youtube#liveBroadcast.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube assigns to uniquely identify the broadcast.
  name: id
  type: string
- description: Basic details about a live broadcast including its title, description, and scheduled start and end times.
  name: snippet
  type: object
- description: Status information about a live broadcast including its privacy status and lifecycle status.
  name: status
  type: object
- description: Detailed settings for a live broadcast including stream configuration, DVR settings, and content configuration.
  name: contentDetails
  type: object
- description: The statistics object contains info about the live broadcast.
  name: statistics
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-broadcast-schema.json
slug: youtube-live-live-broadcast
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveBroadcast
---
