---
description: A playlist resource represents a YouTube playlist.
layout: schema
name: Playlist
properties_list:
- description: Identifies the API resource's type. Value is youtube#playlist.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the playlist.
  name: id
  type: string
- description: Basic details about the playlist such as its title, description, and thumbnails.
  name: snippet
  type: object
- description: The status object contains status information for the playlist.
  name: status
  type: object
- description: The contentDetails object contains information about the playlist content.
  name: contentDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-playlist-schema.json
slug: youtube-data-playlist
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Playlist
---
