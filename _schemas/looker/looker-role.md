---
description: A role defines a set of permissions and model access controls that can be assigned to users and groups.
layout: schema
name: Role
properties_list:
- description: Unique numeric identifier
  name: id
  type: integer
- description: Display name of the role
  name: name
  type: string
- description: ID of the permission set assigned to this role
  name: permission_set_id
  type: integer
- description: ID of the model set assigned to this role
  name: model_set_id
  type: integer
- description: Number of users with this role
  name: user_count
  type: integer
- description: Relative URL for this role
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-role-schema.json
slug: looker-role
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: Role
---
