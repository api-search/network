---
description: ''
layout: schema
name: MeetingUpdateRequest
properties_list:
- description: Meeting topic.
  name: topic
  type: string
- description: Meeting start time.
  name: start_time
  type: string
- description: Meeting duration in minutes.
  name: duration
  type: integer
- description: Email address or user ID to schedule meeting on behalf of.
  name: schedule_for
  type: string
- description: Timezone for start_time.
  name: timezone
  type: string
- description: Meeting passcode.
  name: password
  type: string
- description: Meeting description.
  name: agenda
  type: string
- description: ''
  name: tracking_fields
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-meeting-update-request-schema.json
slug: zoom-meeting-meeting-update-request
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: MeetingUpdateRequest
---
