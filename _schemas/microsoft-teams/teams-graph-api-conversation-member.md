---
description: Represents a member of a team or channel.
layout: schema
name: ConversationMember
properties_list:
- description: Unique membership ID.
  name: id
  type: string
- description: Display name of the member.
  name: displayName
  type: string
- description: Roles of the member.
  name: roles
  type: array
- description: The Azure AD user ID.
  name: userId
  type: string
- description: Email address of the member.
  name: email
  type: string
provider_name: Microsoft Teams
provider_slug: microsoft-teams
schema_file: json-schema/teams-graph-api-conversation-member-schema.json
slug: teams-graph-api-conversation-member
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
title: ConversationMember
---
