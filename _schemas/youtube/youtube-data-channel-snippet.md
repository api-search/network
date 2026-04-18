---
description: Basic details about a channel, including its title, description, and thumbnails.
layout: schema
name: ChannelSnippet
properties_list:
- description: The channel title.
  name: title
  type: string
- description: The channel description.
  name: description
  type: string
- description: The channel's custom URL.
  name: customUrl
  type: string
- description: The date and time that the channel was created.
  name: publishedAt
  type: string
- description: A map of thumbnail images associated with the channel.
  name: thumbnails
  type: object
- description: The country with which the channel is associated.
  name: country
  type: string
- description: The snippet.localized object contains a localized title and description for the channel.
  name: localized
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-channel-snippet-schema.json
slug: youtube-data-channel-snippet
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: ChannelSnippet
---
