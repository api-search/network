---
description: Represents a channel in a team.
layout: schema
name: Channel
properties_list:
- description: Unique identifier for the channel.
  name: id
  type: string
- description: The display name of the channel.
  name: displayName
  type: string
- description: Description of the channel.
  name: description
  type: string
- description: Type of membership for the channel.
  name: membershipType
  type: string
- description: When the channel was created.
  name: createdDateTime
  type: string
- description: URL to the channel in Teams.
  name: webUrl
  type: string
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-channel-schema.json
slug: teams-graph-api-channel
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: Channel
---
