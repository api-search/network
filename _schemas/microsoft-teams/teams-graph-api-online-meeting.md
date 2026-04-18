---
description: Represents an online meeting in Teams.
layout: schema
name: OnlineMeeting
properties_list:
- description: Unique identifier for the meeting.
  name: id
  type: string
- description: Subject of the meeting.
  name: subject
  type: string
- description: Start time of the meeting.
  name: startDateTime
  type: string
- description: End time of the meeting.
  name: endDateTime
  type: string
- description: URL to join the meeting.
  name: joinWebUrl
  type: string
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-online-meeting-schema.json
slug: teams-graph-api-online-meeting
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: OnlineMeeting
---
