---
description: A comment resource contains information about a single YouTube comment.
layout: schema
name: Comment
properties_list:
- description: Identifies the API resource's type. Value is youtube#comment.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the comment.
  name: id
  type: string
- description: The snippet object contains basic details about the comment.
  name: snippet
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-comment-schema.json
slug: youtube-data-comment
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Comment
---
