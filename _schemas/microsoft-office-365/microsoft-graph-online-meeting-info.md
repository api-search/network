---
description: Details for an attendee to join the meeting online.
layout: schema
name: OnlineMeetingInfo
properties_list:
- description: The URL to join the meeting online.
  name: joinUrl
  type: string
- description: The ID of the conference.
  name: conferenceId
  type: string
- description: The toll number to dial for audio conference.
  name: tollNumber
  type: string
- description: The toll-free numbers to dial.
  name: tollFreeNumbers
  type: array
- description: The pre-formatted quick-dial for this call.
  name: quickDial
  type: string
- description: All phone numbers associated with this conference.
  name: phones
  type: array
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-online-meeting-info-schema.json
slug: microsoft-graph-online-meeting-info
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: OnlineMeetingInfo
---
