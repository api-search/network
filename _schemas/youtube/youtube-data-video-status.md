---
description: The status of an uploaded video.
layout: schema
name: VideoStatus
properties_list:
- description: The status of the uploaded video.
  name: uploadStatus
  type: string
- description: The video's privacy status.
  name: privacyStatus
  type: string
- description: The video's license.
  name: license
  type: string
- description: Indicates whether the video can be embedded on another website.
  name: embeddable
  type: boolean
- description: Indicates whether the video's extended statistics on the video's watch page are publicly viewable.
  name: publicStatsViewable
  type: boolean
- description: Indicates whether the video is designated as child-directed.
  name: madeForKids
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-status-schema.json
slug: youtube-data-video-status
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoStatus
---
