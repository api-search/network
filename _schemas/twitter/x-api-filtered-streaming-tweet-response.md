---
description: A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched.
layout: schema
name: FilteredStreamingTweetResponse
properties_list:
- description: ''
  name: data
  type: object
- description: ''
  name: errors
  type: array
- description: ''
  name: includes
  type: object
- description: The list of rules which matched the Tweet
  name: matching_rules
  type: array
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-filtered-streaming-tweet-response-schema.json
slug: x-api-filtered-streaming-tweet-response
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: FilteredStreamingTweetResponse
---
