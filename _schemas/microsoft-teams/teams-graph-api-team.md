---
description: Represents a Microsoft Teams team.
layout: schema
name: Team
properties_list:
- description: Unique identifier for the team.
  name: id
  type: string
- description: The display name of the team.
  name: displayName
  type: string
- description: Description of the team.
  name: description
  type: string
- description: Team visibility.
  name: visibility
  type: string
- description: Whether the team is archived.
  name: isArchived
  type: boolean
- description: When the team was created.
  name: createdDateTime
  type: string
- description: URL to the team in Microsoft Teams.
  name: webUrl
  type: string
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-team-schema.json
slug: teams-graph-api-team
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: Team
---
