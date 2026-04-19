---
description: A Snowflake view
layout: schema
name: View
properties_list:
- description: Name of the view
  name: name
  type: string
- description: Whether or not this view is secure
  name: secure
  type: boolean
- description: Kind of the view, permanent (default) or temporary
  name: kind
  type: string
- description: Whether or not this view can refer to itself using recursive syntax withot requiring a CTE (common table expression)
  name: recursive
  type: boolean
- description: The columns of the view
  name: columns
  type: array
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: Query used to create the view
  name: query
  type: string
- description: Date and time when the view was created.
  name: created_on
  type: string
- description: Database in which the view is stored
  name: database_name
  type: string
- description: Schema in which the view is stored
  name: schema_name
  type: string
- description: Role that owns the view
  name: owner
  type: string
- description: The type of role that owns the view
  name: owner_role_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/view-view-schema.json
slug: view-view
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: View
---
