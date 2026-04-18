---
description: A group resource represents a YouTube Analytics group, which is a custom collection of up to 500 channels, videos, playlists, or assets. You can use groups to simplify retrieving data for multiple resources.
layout: schema
name: Group
properties_list:
- description: Identifies the API resource's type. Value is youtube#group.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the group.
  name: id
  type: string
- description: The snippet object contains basic details about the group.
  name: snippet
  type: object
- description: Describes the content of a YouTube Analytics group in terms of the number of items it contains and the type of items it contains.
  name: contentDetails
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-group-schema.json
slug: youtube-analytics-group
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Group
---
