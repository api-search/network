---
description: A Looker user account. Users have credentials, roles, and can own content such as Looks, dashboards, and queries.
layout: schema
name: User
properties_list:
- description: Unique numeric identifier
  name: id
  type: integer
- description: First name
  name: first_name
  type: string
- description: Last name
  name: last_name
  type: string
- description: Full display name
  name: display_name
  type: string
- description: Email address
  name: email
  type: string
- description: URL of the user's avatar image
  name: avatar_url
  type: string
- description: Whether the user account is disabled
  name: is_disabled
  type: boolean
- description: User's locale setting
  name: locale
  type: string
- description: ID of the user's personal space (folder)
  name: home_space_id
  type: string
- description: ID of the user's personal folder
  name: home_folder_id
  type: string
- description: ID of the user's personal space
  name: personal_space_id
  type: integer
- description: ID of the user's personal folder
  name: personal_folder_id
  type: integer
- description: Whether the user is a Looker employee
  name: presumed_looker_employee
  type: boolean
- description: Whether the user is a verified Looker employee
  name: verified_looker_employee
  type: boolean
- description: Whether user roles are managed externally (e.g. via SAML)
  name: roles_externally_managed
  type: boolean
- description: Whether roles can be assigned directly to this user
  name: allow_direct_roles
  type: boolean
- description: Whether the user can be added to groups
  name: allow_normal_group_membership
  type: boolean
- description: Whether the user inherits roles from groups
  name: allow_roles_from_normal_groups
  type: boolean
- description: Embed group space ID
  name: embed_group_space_id
  type: integer
- description: API3 credentials for this user
  name: credentials_api3
  type: array
- description: Active sessions for this user
  name: sessions
  type: array
- description: IDs of roles assigned to this user
  name: role_ids
  type: array
- description: IDs of groups this user belongs to
  name: group_ids
  type: array
- description: Relative URL for this user
  name: url
  type: string
- description: Timestamp when the user was created
  name: created_at
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-user-schema.json
slug: looker-user
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: User
---
