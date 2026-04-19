---
description: ''
layout: schema
name: MeetingCreateResponse
properties_list:
- description: Unique meeting instance ID.
  name: uuid
  type: string
- description: Meeting ID (meeting number).
  name: id
  type: integer
- description: ID of the meeting host.
  name: host_id
  type: string
- description: Email address of the meeting host.
  name: host_email
  type: string
- description: Meeting topic.
  name: topic
  type: string
- description: Meeting status.
  name: status
  type: string
- description: Meeting start time.
  name: start_time
  type: string
- description: Meeting duration in minutes.
  name: duration
  type: integer
- description: Timezone of the meeting.
  name: timezone
  type: string
- description: Meeting agenda.
  name: agenda
  type: string
- description: Time the meeting was created.
  name: created_at
  type: string
- description: URL for the host to start the meeting.
  name: start_url
  type: string
- description: URL for participants to join the meeting.
  name: join_url
  type: string
- description: Meeting passcode.
  name: password
  type: string
- description: H.323/SIP room system passcode.
  name: h323_password
  type: string
- description: Password for PSTN dial-in.
  name: pstn_password
  type: string
- description: Encrypted passcode for the meeting URL.
  name: encrypted_password
  type: string
- description: ''
  name: occurrences
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-meeting-create-response-schema.json
slug: zoom-meeting-meeting-create-response
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: MeetingCreateResponse
---
