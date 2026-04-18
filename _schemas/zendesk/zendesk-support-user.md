---
description: A Zendesk user representing an end user, agent, or admin in the account.
layout: schema
name: User
properties_list:
- description: Automatically assigned user ID.
  name: id
  type: integer
- description: The API URL of the user.
  name: url
  type: string
- description: The name of the user.
  name: name
  type: string
- description: The primary email address of the user.
  name: email
  type: string
- description: The primary phone number of the user.
  name: phone
  type: string
- description: The user's profile photo.
  name: photo
  type: object
- description: The locale ID of the user.
  name: locale_id
  type: integer
- description: The locale of the user (e.g., en-US).
  name: locale
  type: string
- description: The time zone of the user.
  name: time_zone
  type: string
- description: The ID of the user's default organization.
  name: organization_id
  type: integer
- description: The role of the user.
  name: role
  type: string
- description: The custom role ID for agents with custom roles.
  name: custom_role_id
  type: integer
- description: Whether the user's identity has been verified.
  name: verified
  type: boolean
- description: An external ID for the user from an integrated system.
  name: external_id
  type: string
- description: Tags applied to the user.
  name: tags
  type: array
- description: An alias displayed instead of the agent's name.
  name: alias
  type: string
- description: Whether the user account is active.
  name: active
  type: boolean
- description: Whether the user is shared from a different Zendesk Support instance.
  name: shared
  type: boolean
- description: Whether the user is a shared agent from a different instance.
  name: shared_agent
  type: boolean
- description: Whether the phone number is shared.
  name: shared_phone_number
  type: boolean
- description: The signature text appended to the agent's comments.
  name: signature
  type: string
- description: Details about the user visible only to agents.
  name: details
  type: string
- description: Notes about the user visible only to agents.
  name: notes
  type: string
- description: Whether the agent has restrictions (true for agents in a custom role with restrictions).
  name: restricted_agent
  type: boolean
- description: Whether the user is suspended.
  name: suspended
  type: boolean
- description: The default group ID for the agent.
  name: default_group_id
  type: integer
- description: Whether the user can access the CSV report.
  name: report_csv
  type: boolean
- description: Whether the user can only create private comments (for restricted end users).
  name: only_private_comments
  type: boolean
- description: The ticket access restriction for the agent.
  name: ticket_restriction
  type: string
- description: Whether the user has community moderator privileges.
  name: moderator
  type: boolean
- description: Whether the user is a chat-only agent.
  name: chat_only
  type: boolean
- description: Whether two-factor authentication is enabled.
  name: two_factor_auth_enabled
  type: boolean
- description: Custom user field values (key-value pairs).
  name: user_fields
  type: object
- description: The last time the user signed in (ISO 8601).
  name: last_login_at
  type: string
- description: When the user was created (ISO 8601).
  name: created_at
  type: string
- description: When the user was last updated (ISO 8601).
  name: updated_at
  type: string
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-user-schema.json
slug: zendesk-support-user
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Tickets
title: User
---
