---
consumed_apis:
- teams-graph
description: Workflow capability for team collaboration including managing teams, channels, messaging, members, meetings, and calls. Used by IT administrators, team leads, and developers building Teams integrations.
layout: capability
name: Microsoft Teams Collaboration
operations:
- description: List joined teams.
  method: GET
  name: list-joined-teams
  path: /v1/teams
- description: Create a team.
  method: POST
  name: create-team
  path: /v1/teams
- description: List channels.
  method: GET
  name: list-channels
  path: /v1/channels
- description: Create a channel.
  method: POST
  name: create-channel
  path: /v1/channels
- description: List messages.
  method: GET
  name: list-channel-messages
  path: /v1/messages
- description: Send a message.
  method: POST
  name: send-channel-message
  path: /v1/messages
- description: List members.
  method: GET
  name: list-team-members
  path: /v1/members
- description: Create a meeting.
  method: POST
  name: create-online-meeting
  path: /v1/meetings
personas: []
provider_name: Microsoft Teams
provider_slug: microsoft-teams
search_terms:
- Developer
- list messages from a channel.
- meeting management.
- developers building teams integrations and bots.
- create a channel.
- list channels
- create channel
- productivity
- list channels.
- video conferencing
- list messages.
- create an online meeting.
- list all members of a team.
- list team members
- list members.
- create online meeting
- team management.
- Team Lead
- create team
- team leads managing channels, members, and communication.
- it admins managing teams infrastructure and policies.
- communication
- chat
- send a message.
- create a new channel.
- add a member to a team.
- list joined teams.
- send a message to a channel.
- create a new team.
- add team member
- channel management.
- create a meeting.
- manage teams collaboration workflows.
- create call
- IT Administrator
- list channels in a team.
- send channel message
- list all teams the user has joined.
- member management.
- list joined teams
- microsoft 365
- collaboration
- list channel messages
- create a team.
- microsoft teams
- initiate a call.
- messaging.
slug: team-collaboration
tags:
- Microsoft Teams
- Collaboration
- Communication
tools:
- description: List all teams the user has joined.
  hints:
    openWorld: true
    readOnly: true
  name: list-joined-teams
- description: Create a new team.
  hints:
    readOnly: false
  name: create-team
- description: List channels in a team.
  hints:
    openWorld: true
    readOnly: true
  name: list-channels
- description: Create a new channel.
  hints:
    readOnly: false
  name: create-channel
- description: List messages from a channel.
  hints:
    openWorld: true
    readOnly: true
  name: list-channel-messages
- description: Send a message to a channel.
  hints:
    readOnly: false
  name: send-channel-message
- description: List all members of a team.
  hints:
    openWorld: true
    readOnly: true
  name: list-team-members
- description: Add a member to a team.
  hints:
    readOnly: false
  name: add-team-member
- description: Create an online meeting.
  hints:
    readOnly: false
  name: create-online-meeting
- description: Initiate a call.
  hints:
    readOnly: false
  name: create-call
---
