---
description: A set of permissions that can be assigned to a role
layout: schema
name: PermissionSet
properties_list:
- description: Unique numeric identifier
  name: id
  type: integer
- description: Display name
  name: name
  type: string
- description: List of permission strings
  name: permissions
  type: array
- description: Whether this is a built-in permission set
  name: built_in
  type: boolean
- description: Whether this grants all permissions
  name: all_access
  type: boolean
- description: Relative URL
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-permission-set-schema.json
slug: looker-permission-set
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: PermissionSet
---
