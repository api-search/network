---
description: ''
layout: schema
name: RecordingList
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
- description: Meeting start time.
  name: start_time
  type: string
- description: Timezone.
  name: timezone
  type: string
- description: Meeting duration in minutes.
  name: duration
  type: integer
- description: Total file size of all recordings in bytes.
  name: total_size
  type: integer
- description: Number of recording files.
  name: recording_count
  type: integer
- description: Share URL for the recording.
  name: share_url
  type: string
- description: ''
  name: recording_files
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-recording-list-schema.json
slug: zoom-meeting-recording-list
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: RecordingList
---
