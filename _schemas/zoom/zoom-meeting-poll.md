---
description: ''
layout: schema
name: Poll
properties_list:
- description: Poll ID.
  name: id
  type: integer
- description: Poll title.
  name: title
  type: string
- description: Whether this is an anonymous poll.
  name: anonymous
  type: boolean
- description: Poll status.
  name: status
  type: string
- description: Type of poll. 1 - Poll, 2 - Advanced Poll, 3 - Quiz.
  name: poll_type
  type: integer
- description: List of questions in the poll.
  name: questions
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-poll-schema.json
slug: zoom-meeting-poll
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: Poll
---
