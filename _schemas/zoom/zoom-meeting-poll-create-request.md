---
description: ''
layout: schema
name: PollCreateRequest
properties_list:
- description: Poll title. Maximum 64 characters.
  name: title
  type: string
- description: Whether this is an anonymous poll.
  name: anonymous
  type: boolean
- description: Type of poll. 1 - Poll, 2 - Advanced Poll, 3 - Quiz.
  name: poll_type
  type: integer
- description: List of questions for the poll.
  name: questions
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-poll-create-request-schema.json
slug: zoom-meeting-poll-create-request
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: PollCreateRequest
---
