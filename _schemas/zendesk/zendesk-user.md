---
description: A Zendesk user representing an end user, agent, or admin in the Zendesk Support account. Users are the people who interact with the support system, whether they are customers submitting tickets, agents handling requests, or administrators managing the account. Each user has a role, identity information, and can belong to one or more organizations.
layout: schema
name: Zendesk User
properties_list:
- description: Automatically assigned unique identifier for the user.
  name: id
  type: integer
- description: The API URL of the user resource.
  name: url
  type: string
- description: The full name of the user.
  name: name
  type: string
- description: The primary email address of the user.
  name: email
  type:
  - string
  - 'null'
- description: The primary phone number of the user.
  name: phone
  type:
  - string
  - 'null'
- description: The user's profile photo attachment.
  name: photo
  type:
  - object
  - 'null'
- description: The locale ID for the user, determining their language preferences.
  name: locale_id
  type:
  - integer
  - 'null'
- description: The locale string of the user (e.g., en-US).
  name: locale
  type: string
- description: The IANA time zone of the user (e.g., America/New_York).
  name: time_zone
  type:
  - string
  - 'null'
- description: The ID of the user's default organization.
  name: organization_id
  type:
  - integer
  - 'null'
- description: The role of the user in the Zendesk account.
  name: role
  type: string
- description: The ID of the custom role for agents with non-default permissions.
  name: custom_role_id
  type:
  - integer
  - 'null'
- description: Whether the user's primary identity (email or phone) has been verified.
  name: verified
  type: boolean
- description: An ID from an external system for cross-referencing users.
  name: external_id
  type:
  - string
  - 'null'
- description: Tags applied to the user for segmentation and business rules.
  name: tags
  type: array
- description: An alias displayed to end users instead of the agent's real name.
  name: alias
  type:
  - string
  - 'null'
- description: Whether the user account is currently active.
  name: active
  type: boolean
- description: Whether the user is shared from a different Zendesk Support instance.
  name: shared
  type: boolean
- description: Whether the user is a shared agent from a different Zendesk Support instance.
  name: shared_agent
  type: boolean
- description: Whether the user's phone number is shared with another user.
  name: shared_phone_number
  type:
  - boolean
  - 'null'
- description: The agent's signature text, appended to their comments.
  name: signature
  type:
  - string
  - 'null'
- description: Details about the user, visible only to agents.
  name: details
  type:
  - string
  - 'null'
- description: Internal notes about the user, visible only to agents.
  name: notes
  type:
  - string
  - 'null'
- description: Whether the agent has role-based restrictions.
  name: restricted_agent
  type: boolean
- description: Whether the user account is suspended. Suspended users cannot sign in and their tickets are suspended.
  name: suspended
  type: boolean
- description: The default group ID for the agent.
  name: default_group_id
  type:
  - integer
  - 'null'
- description: Whether the user has permission to access CSV reports.
  name: report_csv
  type: boolean
- description: Whether the user can only create private (internal) comments.
  name: only_private_comments
  type: boolean
- description: The scope of tickets the agent can access.
  name: ticket_restriction
  type:
  - string
  - 'null'
- description: Whether the user has moderator privileges in the community forums.
  name: moderator
  type: boolean
- description: Whether the agent is limited to chat-only access.
  name: chat_only
  type: boolean
- description: Whether two-factor authentication is enabled for the user.
  name: two_factor_auth_enabled
  type:
  - boolean
  - 'null'
- description: Custom user field values as key-value pairs. Keys are the field keys defined via the User Fields API.
  name: user_fields
  type: object
- description: The last time the user signed in, in ISO 8601 format.
  name: last_login_at
  type:
  - string
  - 'null'
- description: When the user was created, in ISO 8601 format.
  name: created_at
  type: string
- description: When the user was last updated, in ISO 8601 format.
  name: updated_at
  type: string
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-user-schema.json
slug: zendesk-user
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
title: Zendesk User
---
