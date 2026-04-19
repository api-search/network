---
description: A Snowflake table
layout: schema
name: Table
properties_list:
- description: Specifies the name for the table, must be unique for the schema in which the table is created
  name: name
  type: string
- description: Table type - permanent, transient, or temporary
  name: kind
  type: string
- description: Specifies one or more columns or column expressions in the table as the clustering key
  name: cluster_by
  type: array
- description: Table has schema evolution enabled or disabled
  name: enable_schema_evolution
  type: boolean
- description: Change tracking is enabled or disabled
  name: change_tracking
  type: boolean
- description: Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table
  name: data_retention_time_in_days
  type: integer
- description: Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table
  name: max_data_extension_time_in_days
  type: integer
- description: Specifies a default collation specification for the columns in the table, including columns added to the table in the future
  name: default_ddl_collation
  type: string
- description: ''
  name: columns
  type: array
- description: ''
  name: constraints
  type: array
- description: Comment for the table
  name: comment
  type: string
- description: Date and time when the table was created.
  name: created_on
  type: string
- description: Database in which the table is stored
  name: database_name
  type: string
- description: Schema in which the table is stored
  name: schema_name
  type: string
- description: Number of rows in the table. Returns NULL for external tables.
  name: rows
  type: integer
- description: Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table
  name: bytes
  type: integer
- description: Role that owns the table
  name: owner
  type: string
- description: Date and time when the table was dropped
  name: dropped_on
  type: string
- description: If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.
  name: automatic_clustering
  type: boolean
- description: If ON, the table has the search optimization service enabled
  name: search_optimization
  type: boolean
- description: Percentage of the table that has been optimized for search.
  name: search_optimization_progress
  type: integer
- description: Number of additional bytes of storage that the search optimization service consumes for this table
  name: search_optimization_bytes
  type: integer
- description: The type of role that owns the object.
  name: owner_role_type
  type: string
- description: Name of the budget if the object is monitored by a budget
  name: budget
  type: string
- description: Type of the table
  name: table_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/table-table-schema.json
slug: table-table
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Table
---
