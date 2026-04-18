---
description: A list of live chat moderator resources for a given live chat.
layout: schema
name: LiveChatModeratorListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#liveChatModeratorListResponse.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The token for the next page of results.
  name: nextPageToken
  type: string
- description: The token for the previous page of results.
  name: prevPageToken
  type: string
- description: Paging details for a list of live streaming resources.
  name: pageInfo
  type: object
- description: A list of moderators that match the request criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-live-live-chat-moderator-list-response-schema.json
slug: youtube-live-live-chat-moderator-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: LiveChatModeratorListResponse
---
