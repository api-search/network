---
description: A video resource represents a YouTube video. The resource contains information about the video's metadata, statistics, content details, status, and player embed information.
layout: schema
name: YouTube Video
properties_list:
- description: The ID that YouTube uses to uniquely identify the video.
  name: id
  type: string
- description: Identifies the API resource's type. The value will be youtube#video.
  name: kind
  type: string
- description: The Etag of this resource, used for cache validation and conditional requests.
  name: etag
  type: string
- description: The snippet object contains basic details about the video, such as its title, description, and category.
  name: snippet
  type: object
- description: The statistics object contains statistics about the video such as the number of times the video has been viewed or liked.
  name: statistics
  type: object
- description: The contentDetails object contains information about the video content, including the length of the video and an indication of whether captions are available.
  name: contentDetails
  type: object
- description: The status object contains information about the video's uploading, processing, and privacy statuses.
  name: status
  type: object
- description: The player object contains information that you would use to play the video in an embedded player.
  name: player
  type: object
- description: The localizations object contains translations of the video's metadata.
  name: localizations
  type: object
- description: The topicDetails object encapsulates information about topics associated with the video.
  name: topicDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-video-schema.json
slug: youtube-video
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: YouTube Video
---
