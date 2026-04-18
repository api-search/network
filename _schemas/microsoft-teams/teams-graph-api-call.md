---
description: Represents a call in Teams.
layout: schema
name: Call
properties_list:
- description: Unique identifier for the call.
  name: id
  type: string
- description: Current call state.
  name: state
  type: string
- description: Direction of the call.
  name: direction
  type: string
- description: Subject of the call.
  name: subject
  type: string
- description: Callback URL for call notifications.
  name: callbackUri
  type: string
- description: Requested communication modalities.
  name: requestedModalities
  type: array
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-call-schema.json
slug: teams-graph-api-call
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: Call
---
