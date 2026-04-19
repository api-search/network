---
description: A Snowflake role
layout: schema
name: Role
properties_list:
- description: Name of the role.
  name: name
  type: string
- description: Comment of the role.
  name: comment
  type: string
- description: Date and time when the role was created.
  name: created_on
  type: string
- description: Specifies the role that owns this role.
  name: owner
  type: string
- description: Specifies whether the role being fetched is the user's default role.
  name: is_default
  type: boolean
- description: Specifies whether the role being fetched is the user's current role.
  name: is_current
  type: boolean
- description: Specifies whether the role used to run the command inherits the specified role.
  name: is_inherited
  type: boolean
- description: The number of users to whom this role has been assigned.
  name: assigned_to_users
  type: integer
- description: The number of roles to which this role has been granted.
  name: granted_to_roles
  type: integer
- description: The number of roles that have been granted to this role.
  name: granted_roles
  type: integer
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/role-role-schema.json
slug: role-role
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Role
---
