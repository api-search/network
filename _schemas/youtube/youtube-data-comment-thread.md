---
description: A commentThread resource contains information about a YouTube comment thread, which comprises a top-level comment and replies.
layout: schema
name: CommentThread
properties_list:
- description: Identifies the API resource's type. Value is youtube#commentThread.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the comment thread.
  name: id
  type: string
- description: The snippet object contains basic details about the comment thread.
  name: snippet
  type: object
- description: The replies object contains a list of replies to the top-level comment.
  name: replies
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-comment-thread-schema.json
slug: youtube-data-comment-thread
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: CommentThread
---
