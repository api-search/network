---
description: A X List is a curated group of accounts.
layout: schema
name: List
properties_list:
- description: ''
  name: created_at
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: follower_count
  type: integer
- description: The unique identifier of this List.
  name: id
  type: string
- description: ''
  name: member_count
  type: integer
- description: The name of this List.
  name: name
  type: string
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: owner_id
  type: string
- description: ''
  name: private
  type: boolean
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-list-schema.json
slug: x-api-list
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: List
---
