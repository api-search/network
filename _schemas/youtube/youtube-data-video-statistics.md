---
description: Statistics about the video such as the number of times the video has been viewed or liked.
layout: schema
name: VideoStatistics
properties_list:
- description: The number of times the video has been viewed.
  name: viewCount
  type: string
- description: The number of users who have indicated that they liked the video.
  name: likeCount
  type: string
- description: The number of users who have indicated that they disliked the video.
  name: dislikeCount
  type: string
- description: The number of users who have added the video to their favorites list.
  name: favoriteCount
  type: string
- description: The number of comments for the video.
  name: commentCount
  type: string
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-statistics-schema.json
slug: youtube-data-video-statistics
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoStatistics
---
