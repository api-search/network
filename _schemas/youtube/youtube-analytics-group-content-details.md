---
description: Describes the content of a YouTube Analytics group in terms of the number of items it contains and the type of items it contains.
layout: schema
name: GroupContentDetails
properties_list:
- description: The number of items in the group.
  name: itemCount
  type: integer
- description: The type of resources contained in the group. Valid values are youtube#channel, youtube#playlist, youtube#video, and youtubePartner#asset.
  name: itemType
  type: string
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-group-content-details-schema.json
slug: youtube-analytics-group-content-details
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: GroupContentDetails
---
