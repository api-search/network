---
description: A Snowflake dynamic table object.
layout: schema
name: DynamicTable
properties_list:
- description: Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created
  name: name
  type: string
- description: Specifies the dynamic table type, permanent (default) or transient.
  name: kind
  type: string
- description: ''
  name: columns
  type: array
- description: Specifies the refresh type for the dynamic table
  name: refresh_mode
  type: string
- description: Specifies the behavior of the initial refresh of the dynamic table
  name: initialize
  type: string
- description: Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table
  name: warehouse
  type: string
- description: Specifies one or more columns or column expressions in the dynamic table as the clustering key
  name: cluster_by
  type: array
- description: Specifies the query whose results the dynamic table should contain
  name: query
  type: string
- description: Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table
  name: data_retention_time_in_days
  type: integer
- description: Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table
  name: max_data_extension_time_in_days
  type: integer
- description: Specifies a comment for the dynamic table.
  name: comment
  type: string
- description: Date and time when the dynamic table was created.
  name: created_on
  type: string
- description: Database in which the dynamic table is stored
  name: database_name
  type: string
- description: Schema in which the dynamic table is stored
  name: schema_name
  type: string
- description: Number of rows in the dynamic table.
  name: rows
  type: integer
- description: Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table
  name: bytes
  type: integer
- description: Scheduling state (RUNNING or SUSPENDED)
  name: scheduling_state
  type: string
- description: If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the dynamic table.
  name: automatic_clustering
  type: boolean
- description: Role that owns the table
  name: owner
  type: string
- description: The type of role that owns the object.
  name: owner_role_type
  type: string
- description: Name of the budget if the object is monitored by a budget
  name: budget
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/dynamic-table-dynamic-table-schema.json
slug: dynamic-table-dynamic-table
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: DynamicTable
---
