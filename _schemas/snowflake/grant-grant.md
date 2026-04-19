---
description: Properties of a grant that can be granted to a role or user.
layout: schema
name: Grant
properties_list:
- description: Privilege type
  name: privileges
  type: array
- description: Can grantee pass this privilege down?
  name: grant_option
  type: boolean
- description: ''
  name: created_on
  type: string
- description: Entity type being granted to
  name: grantee_type
  type: string
- description: Specific name of object being granted to
  name: grantee_name
  type: string
- description: Type of object granted on
  name: securable_type
  type: string
- description: Name of specific object granted on (not name of privilege!)
  name: securable_name
  type: string
- description: Type of role that granted this privilege to this grantee
  name: granted_by_role_type
  type: string
- description: The role that granted this privilege to this grantee
  name: granted_by_name
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/grant-grant-schema.json
slug: grant-grant
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Grant
---
