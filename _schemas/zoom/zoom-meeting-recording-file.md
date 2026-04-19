---
description: ''
layout: schema
name: RecordingFile
properties_list:
- description: Recording file ID.
  name: id
  type: string
- description: Meeting ID.
  name: meeting_id
  type: string
- description: Recording start time.
  name: recording_start
  type: string
- description: Recording end time.
  name: recording_end
  type: string
- description: Recording file type.
  name: file_type
  type: string
- description: File extension.
  name: file_extension
  type: string
- description: File size in bytes.
  name: file_size
  type: number
- description: URL to download the recording file.
  name: download_url
  type: string
- description: URL to play the recording file.
  name: play_url
  type: string
- description: Recording status.
  name: status
  type: string
- description: Recording type.
  name: recording_type
  type: string
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-recording-file-schema.json
slug: zoom-meeting-recording-file
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: RecordingFile
---
