---
description: A subscription resource contains information about a YouTube user's subscription to a channel.
layout: schema
name: Subscription
properties_list:
- description: Identifies the API resource's type. Value is youtube#subscription.
  name: kind
  type: string
- description: The Etag of this resource.
  name: etag
  type: string
- description: The ID that YouTube uses to uniquely identify the subscription.
  name: id
  type: string
- description: The snippet object contains basic details about the subscription.
  name: snippet
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-subscription-schema.json
slug: youtube-data-subscription
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Subscription
---
