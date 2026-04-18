---
description: Basic details about a live broadcast including its title, description, and scheduled start and end times.
layout: schema
name: LiveBroadcastSnippet
properties_list:
- description: The date and time that the broadcast was added to YouTube's live broadcast schedule.
  name: publishedAt
  type: string
- description: The ID of the channel to which this broadcast is affiliated.
  name: channelId
  type: string
- description: The broadcast's title. The title is a required field when inserting a broadcast.
  name: title
  type: string
- description: The broadcast's description.
  name: description
  type: string
- description: A map of thumbnail images associated with the broadcast.
  name: thumbnails
  type: object
- description: The date and time that the broadcast is scheduled to begin.
  name: scheduledStartTime
  type: string
- description: The date and time that the broadcast is scheduled to end.
  name: scheduledEndTime
  type: string
- description: The date and time that the broadcast actually started.
  name: actualStartTime
  type: string
- description: The date and time that the broadcast actually ended.
  name: actualEndTime
  type: string
- description: The live chat ID associated with the broadcast.
  name: liveChatId
  type: string
- description: Indicates whether this broadcast is the default broadcast.
  name: isDefaultBroadcast
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-broadcast-snippet-schema.json
slug: youtube-live-live-broadcast-snippet
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveBroadcastSnippet
---
