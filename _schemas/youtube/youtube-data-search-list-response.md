---
description: A list of search results matching the query criteria.
layout: schema
name: SearchListResponse
properties_list:
- description: Identifies the API resource's type. Value is youtube#searchListResponse.
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
- description: The region code that was used for the search query.
  name: regionCode
  type: string
- description: Paging details for a list operation, including information about the total number of resources and the number per page.
  name: pageInfo
  type: object
- description: A list of results that match the search criteria.
  name: items
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-search-list-response-schema.json
slug: youtube-data-search-list-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: SearchListResponse
---
