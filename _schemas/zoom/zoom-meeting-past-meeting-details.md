---
description: ''
layout: schema
name: PastMeetingDetails
properties_list:
- description: Unique meeting instance ID.
  name: uuid
  type: string
- description: Meeting ID.
  name: id
  type: integer
- description: Host user ID.
  name: host_id
  type: string
- description: Host email address.
  name: host_email
  type: string
- description: Meeting topic.
  name: topic
  type: string
- description: Display name of the meeting host.
  name: user_name
  type: string
- description: Meeting start time.
  name: start_time
  type: string
- description: Meeting end time.
  name: end_time
  type: string
- description: Meeting duration in minutes.
  name: duration
  type: integer
- description: Total meeting minutes across all participants.
  name: total_minutes
  type: integer
- description: Number of participants.
  name: participants_count
  type: integer
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-past-meeting-details-schema.json
slug: zoom-meeting-past-meeting-details
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: PastMeetingDetails
---
