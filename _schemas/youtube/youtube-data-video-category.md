---
description: A videoCategory resource identifies a category that has been or could be associated with uploaded videos.
layout: schema
name: VideoCategory
properties_list:
- description: Identifies the API resource's type. Value is youtube#videoCategory.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the video category.
  name: id
  type: string
- description: The snippet object contains basic details about the video category.
  name: snippet
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-category-schema.json
slug: youtube-data-video-category
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoCategory
---
