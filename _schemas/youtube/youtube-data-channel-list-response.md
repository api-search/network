---
description: A list of channel resources matching the request criteria.
layout: schema
name: ChannelListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#channelListResponse.
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
- description: Paging details for a list operation, including information about the total number of resources and the number per page.
  name: pageInfo
  type: object
- description: A list of channels that match the request criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-channel-list-response-schema.json
slug: youtube-data-channel-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: ChannelListResponse
---
