---
description: CreateContainerRequest schema from Instagram Graph API
layout: schema
name: CreateContainerRequest
properties_list:
- description: Public URL of the image to publish.
  name: image_url
  type: string
- description: Public URL of the video to publish.
  name: video_url
  type: string
- description: Caption text for the media.
  name: caption
  type: string
- description: Type of media to publish.
  name: media_type
  type: string
- description: Set to true if this is an item in a carousel.
  name: is_carousel_item
  type: boolean
- description: Facebook Page ID of a location to tag.
  name: location_id
  type: string
- description: Users to tag in the media.
  name: user_tags
  type: array
- description: ''
  name: access_token
  type: string
provider_name: Instagram
provider_slug: instagram
schema_file: json-schema/instagram-graph-api-create-container-request-schema.json
slug: instagram-graph-api-create-container-request
tags:
- Instagram
- Meta
- Photos
- Social Media
- Videos
- Content Publishing
title: CreateContainerRequest
---
