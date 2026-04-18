---
description: A playlistItem resource identifies another resource, such as a video, that is included in a playlist.
layout: schema
name: PlaylistItem
properties_list:
- description: Identifies the API resource's type. Value is youtube#playlistItem.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the playlist item.
  name: id
  type: string
- description: Basic details about the playlist item such as its title and position in the playlist.
  name: snippet
  type: object
- description: The contentDetails object is included in the resource if the included item is a YouTube video.
  name: contentDetails
  type: object
- description: The status object contains information about the playlist item's privacy status.
  name: status
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-playlist-item-schema.json
slug: youtube-data-playlist-item
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: PlaylistItem
---
