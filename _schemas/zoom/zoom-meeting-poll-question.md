---
description: ''
layout: schema
name: PollQuestion
properties_list:
- description: Question text.
  name: name
  type: string
- description: Question type.
  name: type
  type: string
- description: Whether an answer is required.
  name: answer_required
  type: boolean
- description: Available answer options.
  name: answers
  type: array
- description: Correct answers for quiz type polls.
  name: right_answers
  type: array
- description: Prompts for matching and rank order question types.
  name: prompts
  type: array
- description: Minimum rating value for rating scale questions.
  name: rating_min_value
  type: integer
- description: Maximum rating value for rating scale questions.
  name: rating_max_value
  type: integer
- description: Label for minimum rating value.
  name: rating_min_label
  type: string
- description: Label for maximum rating value.
  name: rating_max_label
  type: string
- description: Minimum characters for short/long answer questions.
  name: answer_min_character
  type: integer
- description: Maximum characters for short/long answer questions.
  name: answer_max_character
  type: integer
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-poll-question-schema.json
slug: zoom-meeting-poll-question
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: PollQuestion
---
