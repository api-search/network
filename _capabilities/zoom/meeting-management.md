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
- chat
- delete a meeting permanently.
- get past meeting details
- get details of a past meeting.
- create poll
- get recordings for a meeting.
- delete recordings
- delete all recordings for a meeting.
- collaboration
- communications
- list polls
- meeting poll management.
- delete a meeting.
- videos
- update a meeting.
- update livestream
- meetings
- delete recordings for a meeting.
- create a new meeting.
- list participants of a live or past meeting.
- webinars
- update a meeting's live stream configuration.
- get recordings
- add a registrant to a meeting.
- list all registrants for a meeting.
- get meeting details.
- add registrant
- list all polls for a meeting.
- meeting recording management.
- get meeting
- list registrants for a meeting.
- meeting lifecycle management.
- video conferencing
- update meeting
- create a new meeting for a user.
- meeting registration management.
- list polls for a meeting.
- zoom
- delete meeting
- create meeting
- retrieve details of a specific meeting.
- list all meetings for a user.
- list registrants
- create a poll for a meeting.
- individual meeting operations.
- list all meetings scheduled for a user.
- list participants
- list meetings
- update meeting details.
- get all recordings for a meeting.
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
