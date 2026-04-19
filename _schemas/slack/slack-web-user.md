---
description: A Slack user object representing a workspace member with their profile, roles, and settings.
layout: schema
name: User
properties_list:
- description: The unique identifier for this user.
  name: id
  type: string
- description: The workspace team ID this user belongs to.
  name: team_id
  type: string
- description: The user's username.
  name: name
  type: string
- description: Whether the user has been deactivated.
  name: deleted
  type: boolean
- description: A hex color code used in certain client displays for this user.
  name: color
  type: string
- description: The user's real name.
  name: real_name
  type: string
- description: The user's timezone identifier (e.g., "America/Los_Angeles").
  name: tz
  type: string
- description: Descriptive label for the user's timezone.
  name: tz_label
  type: string
- description: The user's timezone offset from UTC in seconds.
  name: tz_offset
  type: integer
- description: The user's profile information.
  name: profile
  type: object
- description: Whether the user is a workspace admin.
  name: is_admin
  type: boolean
- description: Whether the user is a workspace owner.
  name: is_owner
  type: boolean
- description: Whether the user is the primary workspace owner.
  name: is_primary_owner
  type: boolean
- description: Whether the user is a guest with single-channel access.
  name: is_restricted
  type: boolean
- description: Whether the user is a single-channel guest.
  name: is_ultra_restricted
  type: boolean
- description: Whether the user is a bot.
  name: is_bot
  type: boolean
- description: Whether the user is an app user.
  name: is_app_user
  type: boolean
- description: Unix timestamp of when the user was last updated.
  name: updated
  type: integer
- description: Whether the user has two-factor authentication enabled.
  name: has_2fa
  type: boolean
- description: IETF language code for the user. Only included when specifically requested.
  name: locale
  type: string
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-web-user-schema.json
slug: slack-web-user
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: User
---
