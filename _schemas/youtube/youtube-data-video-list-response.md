---
description: A list of video resources matching the request criteria.
layout: schema
name: VideoListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#videoListResponse.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The token that can be used as the pageToken parameter to retrieve the next page of results in the result set.
  name: nextPageToken
  type: string
- description: The token that can be used as the pageToken parameter to retrieve the previous page of results in the result set.
  name: prevPageToken
  type: string
- description: Paging details for a list operation, including information about the total number of resources and the number per page.
  name: pageInfo
  type: object
- description: A list of videos that match the request criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-list-response-schema.json
slug: youtube-data-video-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoListResponse
---
