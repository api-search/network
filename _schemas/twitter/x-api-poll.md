---
description: Represent a Poll attached to a Tweet.
layout: schema
name: Poll
properties_list:
- description: ''
  name: duration_minutes
  type: integer
- description: ''
  name: end_datetime
  type: string
- description: Unique identifier of this poll.
  name: id
  type: string
- description: ''
  name: options
  type: array
- description: ''
  name: voting_status
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-poll-schema.json
slug: x-api-poll
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: Poll
---
