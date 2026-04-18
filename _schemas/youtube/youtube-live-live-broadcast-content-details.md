---
description: Detailed settings for a live broadcast including stream configuration, DVR settings, and content configuration.
layout: schema
name: LiveBroadcastContentDetails
properties_list:
- description: The ID of the stream that is bound to the broadcast.
  name: boundStreamId
  type: string
- description: The date and time that the live stream referenced by boundStreamId was last updated.
  name: boundStreamLastUpdateTimeMs
  type: string
- description: The monitorStream object contains information about the monitor stream, which the broadcaster can use to review the event content before the broadcast stream is shown publicly.
  name: monitorStream
  type: object
- description: Indicates whether the broadcast video can be played in an embedded player.
  name: enableEmbed
  type: boolean
- description: Indicates whether the broadcast enables DVR controls. DVR controls enable the viewer to control the video playback experience by pausing, rewinding, or fast forwarding portions of the broadcast.
  name: enableDvr
  type: boolean
- description: Indicates whether YouTube should enable content encryption for the broadcast.
  name: enableContentEncryption
  type: boolean
- description: Indicates whether the broadcast should automatically begin with an in-stream slate when you update the broadcast's status to live.
  name: startWithSlate
  type: boolean
- description: Indicates whether the broadcast has captions enabled.
  name: closedCaptionsType
  type: string
- description: Indicates whether this broadcast has low latency enabled.
  name: enableLowLatency
  type: boolean
- description: Indicates latency preference for the broadcast. The options are ultraLow, low, and normal.
  name: latencyPreference
  type: string
- description: This setting indicates whether the broadcast should automatically begin streaming.
  name: enableAutoStart
  type: boolean
- description: Indicates whether the broadcast should automatically stop streaming.
  name: enableAutoStop
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-broadcast-content-details-schema.json
slug: youtube-live-live-broadcast-content-details
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveBroadcastContentDetails
---
