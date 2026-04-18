---
description: A search result contains information about a YouTube video, channel, or playlist that matches the search query.
layout: schema
name: SearchResult
properties_list:
- description: Identifies the API resource's type. Value is youtube#searchResult.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The id object contains information that can be used to uniquely identify the resource that matches the search request.
  name: id
  type: object
- description: The snippet object contains basic details about a search result, such as its title or description.
  name: snippet
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-search-result-schema.json
slug: youtube-data-search-result
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: SearchResult
---
