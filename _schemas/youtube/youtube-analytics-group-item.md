---
description: A groupItem resource identifies a resource, such as a video, channel, or playlist, that is part of a group. A group can contain a maximum of 500 items and only items of the same type (videos, channels, playlists, or assets).
layout: schema
name: GroupItem
properties_list:
- description: Identifies the API resource's type. Value is youtube#groupItem.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the groupItem resource.
  name: id
  type: string
- description: The ID that YouTube uses to uniquely identify the group that contains the item.
  name: groupId
  type: string
- description: The resource object contains information that identifies the item being added to the group.
  name: resource
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-group-item-schema.json
slug: youtube-analytics-group-item
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: GroupItem
---
