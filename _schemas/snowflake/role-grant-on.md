---
description: ''
layout: schema
name: GrantOn
properties_list:
- description: Date and time when the grant was created
  name: created_on
  type: string
- description: The name of the privilege
  name: privilege
  type: string
- description: The type of of the role
  name: granted_on
  type: string
- description: The name of the role
  name: name
  type: string
- description: The type of the grantee
  name: granted_to
  type: string
- description: The name of the grantee
  name: grantee_name
  type: string
- description: If true, allows the recipient role to grant the privileges to other roles.
  name: grant_option
  type: string
- description: The role that granted this privilege to this grantee
  name: granted_by
  type: string
- description: Type of the role that granted this privilege to this grantee
  name: granted_by_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/role-grant-on-schema.json
slug: role-grant-on
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: GrantOn
---
