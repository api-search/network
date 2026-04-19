---
description: ''
layout: schema
name: RegistrantCreateResponse
properties_list:
- description: Meeting ID.
  name: id
  type: integer
- description: Registrant ID.
  name: registrant_id
  type: string
- description: Meeting start time.
  name: start_time
  type: string
- description: Meeting topic.
  name: topic
  type: string
- description: Unique join URL for this registrant.
  name: join_url
  type: string
- description: Participant PIN code for phone dial-in.
  name: participant_pin_code
  type: integer
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-registrant-create-response-schema.json
slug: zoom-meeting-registrant-create-response
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: RegistrantCreateResponse
---
