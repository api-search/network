---
description: ''
layout: schema
name: RegistrantList
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
- description: Total number of registrant records.
  name: total_records
  type: integer
- description: Pagination token for the next page.
  name: next_page_token
  type: string
- description: List of registrant objects.
  name: registrants
  type: array
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-registrant-list-schema.json
slug: zoom-meeting-registrant-list
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: RegistrantList
---
