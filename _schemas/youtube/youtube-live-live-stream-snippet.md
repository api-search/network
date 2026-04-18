---
description: Basic details about a live stream including its title, description, and channel association.
layout: schema
name: LiveStreamSnippet
properties_list:
- description: The ID of the channel to which this stream is affiliated.
  name: channelId
  type: string
- description: The stream's title. The value must be between 1 and 128 characters long.
  name: title
  type: string
- description: The stream's description. The value cannot be longer than 10000 characters.
  name: description
  type: string
- description: The date and time that the stream was created.
  name: publishedAt
  type: string
- description: Indicates whether this stream is the default stream.
  name: isDefaultStream
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-stream-snippet-schema.json
slug: youtube-live-live-stream-snippet
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveStreamSnippet
---
