---
description: ''
layout: schema
name: GrantOf
properties_list:
- description: Date and time when the grant was created
  name: created_on
  type: string
- description: The name of the role
  name: role
  type: string
- description: The type of the grantee, can be USER or ROLE
  name: granted_to
  type: string
- description: The name of the grantee
  name: grantee_name
  type: string
- description: The role that granted this role to this grantee
  name: granted_by
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/role-grant-of-schema.json
slug: role-grant-of
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: GrantOf
---
