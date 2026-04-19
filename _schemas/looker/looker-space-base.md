---
description: Basic space (folder) information
layout: schema
name: SpaceBase
properties_list:
- description: Unique identifier
  name: id
  type: string
- description: Display name
  name: name
  type: string
- description: Parent space ID
  name: parent_id
  type: string
- description: Whether this is the shared root space
  name: is_shared_root
  type: boolean
- description: Whether this is the users root space
  name: is_users_root
  type: boolean
- description: Whether this is a user's personal root space
  name: is_user_root
  type: boolean
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-space-base-schema.json
slug: looker-space-base
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: SpaceBase
---
