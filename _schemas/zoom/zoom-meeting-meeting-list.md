---
description: ''
layout: schema
name: MeetingList
properties_list:
- description: Total number of pages.
  name: page_count
  type: integer
- description: Current page number.
  name: page_number
  type: integer
- description: Number of records per page.
  name: page_size
  type: integer
- description: Total number of meeting records.
  name: total_records
  type: integer
- description: Token for the next page of results.
  name: next_page_token
  type: string
- description: List of meeting objects.
  name: meetings
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-meeting-list-schema.json
slug: zoom-meeting-meeting-list
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: MeetingList
---
