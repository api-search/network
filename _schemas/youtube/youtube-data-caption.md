---
description: A caption resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.
layout: schema
name: Caption
properties_list:
- description: Identifies the API resource's type. Value is youtube#caption.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the caption track.
  name: id
  type: string
- description: The snippet object contains basic details about the caption.
  name: snippet
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-caption-schema.json
slug: youtube-data-caption
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Caption
---
