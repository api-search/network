---
description: Basic folder information
layout: schema
name: FolderBase
properties_list:
- description: Unique identifier
  name: id
  type: string
- description: Display name
  name: name
  type: string
- description: Parent folder ID
  name: parent_id
  type: string
- description: Content metadata ID
  name: content_metadata_id
  type: integer
- description: Whether this is the shared root folder
  name: is_shared_root
  type: boolean
- description: Whether this is the users root folder
  name: is_users_root
  type: boolean
- description: Whether this is a user's personal root folder
  name: is_user_root
  type: boolean
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-folder-base-schema.json
slug: looker-folder-base
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: FolderBase
---
