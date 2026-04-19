---
description: ''
layout: schema
name: Grant
properties_list:
- description: Type of the securable to be granted.
  name: securable_type
  type: string
- description: If true, allows the recipient role to grant the privileges to other roles.
  name: grant_option
  type: boolean
- description: List of privileges to be granted.
  name: privileges
  type: array
- description: Date and time when the grant was created
  name: created_on
  type: string
- description: The role that granted this privilege to this grantee
  name: granted_by
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/role-grant-schema.json
slug: role-grant
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Grant
---
