---
description: ''
layout: schema
name: MeetingSummary
properties_list:
- description: Unique meeting instance ID.
  name: uuid
  type: string
- description: Meeting ID (meeting number).
  name: id
  type: integer
- description: ID of the user who is the meeting host.
  name: host_id
  type: string
- description: Meeting topic.
  name: topic
  type: string
- description: Meeting start time in UTC.
  name: start_time
  type: string
- description: Meeting duration in minutes.
  name: duration
  type: integer
- description: Timezone for the meeting start time.
  name: timezone
  type: string
- description: Time the meeting was created.
  name: created_at
  type: string
- description: URL for participants to join the meeting.
  name: join_url
  type: string
- description: Meeting agenda or description.
  name: agenda
  type: string
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-meeting-summary-schema.json
slug: zoom-meeting-meeting-summary
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: MeetingSummary
---
