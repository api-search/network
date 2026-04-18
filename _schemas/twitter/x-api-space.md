---
description: ''
layout: schema
name: Space
properties_list:
- description: Creation time of the Space.
  name: created_at
  type: string
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: creator_id
  type: string
- description: End time of the Space.
  name: ended_at
  type: string
- description: The user ids for the hosts of the Space.
  name: host_ids
  type: array
- description: The unique identifier of this Space.
  name: id
  type: string
- description: An array of user ids for people who were invited to a Space.
  name: invited_user_ids
  type: array
- description: Denotes if the Space is a ticketed Space.
  name: is_ticketed
  type: boolean
- description: The language of the Space.
  name: lang
  type: string
- description: The number of participants in a Space.
  name: participant_count
  type: integer
- description: A date time stamp for when a Space is scheduled to begin.
  name: scheduled_start
  type: string
- description: An array of user ids for people who were speakers in a Space.
  name: speaker_ids
  type: array
- description: When the Space was started as a date string.
  name: started_at
  type: string
- description: The current state of the Space.
  name: state
  type: string
- description: The number of people who have either purchased a ticket or set a reminder for this Space.
  name: subscriber_count
  type: integer
- description: The title of the Space.
  name: title
  type: string
- description: The topics of a Space, as selected by its creator.
  name: topics
  type: array
- description: When the Space was last updated.
  name: updated_at
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-space-schema.json
slug: x-api-space
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: Space
---
