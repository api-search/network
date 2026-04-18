---
description: DmEvent schema from X API v2
layout: schema
name: DmEvent
properties_list:
- description: Specifies the type of attachments (if any) present in this DM.
  name: attachments
  type: object
- description: ''
  name: cashtags
  type: array
- description: ''
  name: created_at
  type: string
- description: Unique identifier of a DM conversation. This can either be a numeric string, or a pair of numeric strings separated by a '-' character in the case of one-on-one DM Conversations.
  name: dm_conversation_id
  type: string
- description: ''
  name: event_type
  type: string
- description: ''
  name: hashtags
  type: array
- description: Unique identifier of a DM Event.
  name: id
  type: string
- description: ''
  name: mentions
  type: array
- description: A list of participants for a ParticipantsJoin or ParticipantsLeave event_type.
  name: participant_ids
  type: array
- description: A list of Posts this DM refers to.
  name: referenced_tweets
  type: array
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: sender_id
  type: string
- description: ''
  name: text
  type: string
- description: ''
  name: urls
  type: array
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-dm-event-schema.json
slug: x-api-dm-event
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: DmEvent
---
