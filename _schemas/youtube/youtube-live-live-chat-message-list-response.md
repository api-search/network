---
description: A list of live chat message resources for a given broadcast.
layout: schema
name: LiveChatMessageListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#liveChatMessageListResponse.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The token for the next page of results.
  name: nextPageToken
  type: string
- description: The amount of time the client should wait before polling again, in milliseconds.
  name: pollingIntervalMillis
  type: integer
- description: The date and time when the underlying stream went offline.
  name: offlineAt
  type: string
- description: Paging details for a list of live streaming resources.
  name: pageInfo
  type: object
- description: A list of chat messages that match the request criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-chat-message-list-response-schema.json
slug: youtube-live-live-chat-message-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveChatMessageListResponse
---
