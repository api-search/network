---
description: A list of group resources matching the request criteria.
layout: schema
name: GroupListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#groupListResponse.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The token for the next page of results in the result set.
  name: nextPageToken
  type: string
- description: A list of groups that match the request criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-group-list-response-schema.json
slug: youtube-analytics-group-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: GroupListResponse
---
