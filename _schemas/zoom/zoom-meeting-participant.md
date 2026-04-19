---
description: ''
layout: schema
name: Participant
properties_list:
- description: Participant UUID.
  name: id
  type: string
- description: Participant user ID if the participant is a Zoom user.
  name: user_id
  type: string
- description: Participant display name.
  name: name
  type: string
- description: Participant email address.
  name: user_email
  type: string
- description: Time the participant joined the meeting.
  name: join_time
  type: string
- description: Time the participant left the meeting.
  name: leave_time
  type: string
- description: Participant duration in the meeting (seconds).
  name: duration
  type: integer
- description: Registrant ID if the participant registered.
  name: registrant_id
  type: string
- description: Whether failover occurred for this participant.
  name: failover
  type: boolean
- description: Participant status.
  name: status
  type: string
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-participant-schema.json
slug: zoom-meeting-participant
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: Participant
---
