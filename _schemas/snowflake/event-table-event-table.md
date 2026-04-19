---
description: A Snowflake event table
layout: schema
name: EventTable
properties_list:
- description: Name of the event table
  name: name
  type: string
- description: Cluster key column(s) or expression
  name: cluster_by
  type: array
- description: number of days to retain the old version of deleted/updated data
  name: data_retention_time_in_days
  type: integer
- description: Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.
  name: max_data_extension_time_in_days
  type: integer
- description: True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.
  name: change_tracking
  type: boolean
- description: Collation that is used for all the new columns created by the DDL statements (if not specified)
  name: default_ddl_collation
  type: string
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: Date and time when the event table was created.
  name: created_on
  type: string
- description: Database in which the event table is stored
  name: database_name
  type: string
- description: Schema in which the event table is stored
  name: schema_name
  type: string
- description: Role that owns the event table
  name: owner
  type: string
- description: The type of role that owns the event table
  name: owner_role_type
  type: string
- description: Number of rows in the table.
  name: rows
  type: integer
- description: Number of bytes that will be scanned if the entire table is scanned in a query.Note that this number may be different than the number of actual physical bytes stored on-disk for the table
  name: bytes
  type: integer
- description: If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.
  name: automatic_clustering
  type: boolean
- description: If ON, the table has the search optimization service enabled
  name: search_optimization
  type: boolean
- description: Percentage of the table that has been optimized for search
  name: search_optimization_progress
  type: integer
- description: Number of additional bytes of storage that the search optimization service consumes for this table
  name: search_optimization_bytes
  type: integer
- description: ''
  name: columns
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/event-table-event-table-schema.json
slug: event-table-event-table
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: EventTable
---
