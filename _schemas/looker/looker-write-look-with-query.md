---
description: Writable fields for creating or updating a Look
layout: schema
name: WriteLookWithQuery
properties_list:
- description: Display title
  name: title
  type: string
- description: Description of the Look
  name: description
  type: string
- description: Space (folder) ID to place the Look in
  name: space_id
  type: string
- description: Folder ID to place the Look in
  name: folder_id
  type: string
- description: ID of the query to use
  name: query_id
  type: integer
- description: Whether the Look is public
  name: public
  type: boolean
- description: Whether to auto-run the query on load
  name: is_run_on_load
  type: boolean
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-write-look-with-query-schema.json
slug: looker-write-look-with-query
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: WriteLookWithQuery
---
