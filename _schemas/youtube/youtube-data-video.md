---
description: A video resource represents a YouTube video.
layout: schema
name: Video
properties_list:
- description: Identifies the API resource's type. Value is youtube#video.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the video.
  name: id
  type: string
- description: Basic details about a video, including its title, description, tags, and category.
  name: snippet
  type: object
- description: Information about the video content, including the length of the video and an indication of whether captions are available.
  name: contentDetails
  type: object
- description: The status of an uploaded video.
  name: status
  type: object
- description: Statistics about the video such as the number of times the video has been viewed or liked.
  name: statistics
  type: object
- description: Information used to play the video.
  name: player
  type: object
- description: The localizations object contains translations of the video's metadata.
  name: localizations
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-schema.json
slug: youtube-data-video
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Video
---
