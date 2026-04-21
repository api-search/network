---
consumed_apis:
- zoom-meeting
description: Unified workflow for managing the complete Zoom meeting lifecycle including scheduling, registrants, polls, participants, recordings, and live streaming. Used by meeting organizers, administrators, and automation tools.
layout: capability
name: Zoom Meeting Management
operations:
- description: List all meetings for a user.
  method: GET
  name: list-meetings
  path: /v1/meetings
- description: Create a new meeting.
  method: POST
  name: create-meeting
  path: /v1/meetings
- description: Get meeting details.
  method: GET
  name: get-meeting
  path: /v1/meetings/{meetingId}
- description: Update a meeting.
  method: PATCH
  name: update-meeting
  path: /v1/meetings/{meetingId}
- description: Delete a meeting.
  method: DELETE
  name: delete-meeting
  path: /v1/meetings/{meetingId}
- description: List registrants for a meeting.
  method: GET
  name: list-registrants
  path: /v1/registrants
- description: Add a registrant to a meeting.
  method: POST
  name: add-registrant
  path: /v1/registrants
- description: List polls for a meeting.
  method: GET
  name: list-polls
  path: /v1/polls
- description: Create a poll for a meeting.
  method: POST
  name: create-poll
  path: /v1/polls
- description: Get recordings for a meeting.
  method: GET
  name: get-recordings
  path: /v1/recordings
- description: Delete recordings for a meeting.
  method: DELETE
  name: delete-recordings
  path: /v1/recordings
personas: []
provider_name: Zoom
provider_slug: zoom
search_terms:
- add registrant
- update meeting details.
- delete a meeting permanently.
- list participants
- get recordings
- delete recordings for a meeting.
- webinars
- delete all recordings for a meeting.
- update a meeting.
- create a poll for a meeting.
- list all meetings scheduled for a user.
- meeting lifecycle management.
- list all meetings for a user.
- list meetings
- meeting registration management.
- video conferencing
- list all polls for a meeting.
- communications
- get meeting details.
- meetings
- list registrants
- retrieve details of a specific meeting.
- delete a meeting.
- get all recordings for a meeting.
- list polls for a meeting.
- chat
- meeting poll management.
- create meeting
- list registrants for a meeting.
- delete recordings
- list all registrants for a meeting.
- get details of a past meeting.
- meeting recording management.
- get recordings for a meeting.
- update a meeting's live stream configuration.
- collaboration
- individual meeting operations.
- update livestream
- create a new meeting.
- list participants of a live or past meeting.
- get meeting
- add a registrant to a meeting.
- create a new meeting for a user.
- videos
- create poll
- zoom
- update meeting
- list polls
- delete meeting
- get past meeting details
slug: meeting-management
tags:
- Zoom
- Meetings
- Video Conferencing
- Collaboration
tools:
- description: List all meetings scheduled for a user.
  hints:
    openWorld: true
    readOnly: true
  name: list-meetings
- description: Create a new meeting for a user.
  hints:
    readOnly: false
  name: create-meeting
- description: Retrieve details of a specific meeting.
  hints:
    readOnly: true
  name: get-meeting
- description: Update meeting details.
  hints:
    idempotent: true
    readOnly: false
  name: update-meeting
- description: Delete a meeting permanently.
  hints:
    destructive: true
    idempotent: true
  name: delete-meeting
- description: List all registrants for a meeting.
  hints:
    readOnly: true
  name: list-registrants
- description: Add a registrant to a meeting.
  hints:
    readOnly: false
  name: add-registrant
- description: List all polls for a meeting.
  hints:
    readOnly: true
  name: list-polls
- description: Create a poll for a meeting.
  hints:
    readOnly: false
  name: create-poll
- description: List participants of a live or past meeting.
  hints:
    readOnly: true
  name: list-participants
- description: Get all recordings for a meeting.
  hints:
    readOnly: true
  name: get-recordings
- description: Delete all recordings for a meeting.
  hints:
    destructive: true
    idempotent: true
  name: delete-recordings
- description: Update a meeting's live stream configuration.
  hints:
    idempotent: true
    readOnly: false
  name: update-livestream
- description: Get details of a past meeting.
  hints:
    readOnly: true
  name: get-past-meeting-details
---
