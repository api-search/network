---
description: Status information about a live broadcast including its privacy status and lifecycle status.
layout: schema
name: LiveBroadcastStatus
properties_list:
- description: The broadcast's status as it relates to the lifecycle of the broadcast.
  name: lifeCycleStatus
  type: string
- description: The broadcast's privacy status.
  name: privacyStatus
  type: string
- description: The broadcast's recording status.
  name: recordingStatus
  type: string
- description: Indicates whether the broadcast is designated as child-directed.
  name: madeForKids
  type: boolean
- description: Indicates whether the channel owner has designated the broadcast as being made for kids.
  name: selfDeclaredMadeForKids
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-broadcast-status-schema.json
slug: youtube-live-live-broadcast-status
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveBroadcastStatus
---
