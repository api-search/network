---
description: A liveChatMessage resource represents a chat message in a YouTube live broadcast.
layout: schema
name: LiveChatMessage
properties_list:
- description: Identifies the API resource's type. Value is youtube#liveChatMessage.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube assigns to uniquely identify the message.
  name: id
  type: string
- description: The snippet object contains basic details about the message.
  name: snippet
  type: object
- description: The authorDetails object contains basic details about the user that posted this message.
  name: authorDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-chat-message-schema.json
slug: youtube-live-live-chat-message
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveChatMessage
---
