---
description: A channel resource represents a YouTube channel.
layout: schema
name: Channel
properties_list:
- description: Identifies the API resource's type. Value is youtube#channel.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the channel.
  name: id
  type: string
- description: Basic details about a channel, including its title, description, and thumbnails.
  name: snippet
  type: object
- description: Statistics about a YouTube channel.
  name: statistics
  type: object
- description: The contentDetails object encapsulates information about the channel's content.
  name: contentDetails
  type: object
- description: The brandingSettings object encapsulates information about the branding of the channel.
  name: brandingSettings
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-channel-schema.json
slug: youtube-data-channel
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Channel
---
