---
description: A channel resource represents a YouTube channel. It contains information about a YouTube channel, including its metadata, statistics, content details, and branding settings.
layout: schema
name: YouTube Channel
properties_list:
- description: The ID that YouTube uses to uniquely identify the channel.
  name: id
  type: string
- description: Identifies the API resource's type. The value will be youtube#channel.
  name: kind
  type: string
- description: The Etag of this resource, used for cache validation and conditional requests.
  name: etag
  type: string
- description: The snippet object contains basic details about the channel, such as its title, description, and thumbnail images.
  name: snippet
  type: object
- description: The statistics object encapsulates statistics for the channel.
  name: statistics
  type: object
- description: The contentDetails object encapsulates information about the channel's content.
  name: contentDetails
  type: object
- description: The brandingSettings object encapsulates information about the branding of the channel.
  name: brandingSettings
  type: object
- description: The status object encapsulates information about the privacy status of the channel.
  name: status
  type: object
- description: The localizations object encapsulates translations of the channel's metadata.
  name: localizations
  type: object
- description: The topicDetails object encapsulates information about topics associated with the channel.
  name: topicDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-channel-schema.json
slug: youtube-channel
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: YouTube Channel
---
