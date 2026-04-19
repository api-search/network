---
description: A Snowflake virtual warehouse provides the compute resources required to execute queries and perform DML operations. A warehouse can be started, suspended, resized, and configured for auto-suspend and auto-resume.
layout: schema
name: Snowflake Warehouse
properties_list:
- description: Identifier for the virtual warehouse. Must be unique within the account.
  name: name
  type: string
- description: Type of warehouse specifying the compute resource architecture.
  name: warehouse_type
  type: string
- description: Size of the warehouse determining the number of compute resources per cluster.
  name: warehouse_size
  type: string
- description: When resizing a warehouse, block the return of the ALTER WAREHOUSE command until the resize has finished provisioning all its compute resources.
  name: wait_for_completion
  type: string
- description: Specifies the maximum number of clusters for a multi-cluster warehouse. For a single-cluster warehouse, this value is 1.
  name: max_cluster_count
  type: integer
- description: Specifies the minimum number of clusters for a multi-cluster warehouse. For a single-cluster warehouse, this value is 1.
  name: min_cluster_count
  type: integer
- description: Scaling policy for a multi-cluster warehouse that determines when additional clusters are started or shut down.
  name: scaling_policy
  type: string
- description: Number of seconds of inactivity after which a warehouse is automatically suspended. A value of 0 means the warehouse is never automatically suspended.
  name: auto_suspend
  type: integer
- description: Specifies whether to automatically resume a warehouse when a SQL statement is submitted to it.
  name: auto_resume
  type: string
- description: Specifies whether the warehouse is created initially in the Suspended state.
  name: initially_suspended
  type: string
- description: Specifies the name of a resource monitor that is explicitly assigned to the warehouse. When a resource monitor is explicitly assigned, the monitor controls the monthly credits used by the warehouse.
  name: resource_monitor
  type: string
- description: Specifies a comment for the warehouse.
  name: comment
  type: string
- description: Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources.
  name: enable_query_acceleration
  type: string
- description: Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size.
  name: query_acceleration_max_scale_factor
  type: integer
- description: Object parameter that specifies the concurrency level for SQL statements executed by a warehouse cluster.
  name: max_concurrency_level
  type: integer
- description: Object parameter that specifies the time, in seconds, a SQL statement can be queued on a warehouse before it is canceled by the system.
  name: statement_queued_timeout_in_seconds
  type: integer
- description: Object parameter that specifies the time, in seconds, after which a running SQL statement is canceled by the system.
  name: statement_timeout_in_seconds
  type: integer
- description: Credit limit that can be consumed by the warehouse.
  name: warehouse_credit_limit
  type: integer
- description: Target statement size for adaptive warehouses.
  name: target_statement_size
  type: string
- description: The current state of the warehouse.
  name: state
  type: string
- description: Number of clusters currently started.
  name: started_clusters
  type: integer
- description: Number of SQL statements that are being executed by the warehouse.
  name: running
  type: integer
- description: Number of SQL statements that are queued for the warehouse.
  name: queued
  type: integer
- description: Whether the warehouse is the default for the current user.
  name: is_default
  type: boolean
- description: Whether the warehouse is in use for the session. Only one warehouse can be in use at a time for a session.
  name: is_current
  type: boolean
- description: Percentage of the warehouse compute resources that are provisioned and available.
  name: available
  type: string
- description: Percentage of the warehouse compute resources that are in the process of provisioning.
  name: provisioning
  type: string
- description: Percentage of the warehouse compute resources that are executing SQL statements but will be shut down once the queries complete.
  name: quiescing
  type: string
- description: Percentage of the warehouse compute resources that are in a state other than available, provisioning, or quiescing.
  name: other
  type: string
- description: Date and time when the warehouse was created.
  name: created_on
  type: string
- description: Date and time when the warehouse was last started or restarted.
  name: resumed_on
  type: string
- description: Date and time when the warehouse was last updated, which includes changing any of the properties of the warehouse or changing the state.
  name: updated_on
  type: string
- description: Role that owns the warehouse.
  name: owner
  type: string
- description: The type of role that owns the object.
  name: owner_role_type
  type: string
- description: Budget associated with the warehouse.
  name: budget
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-warehouse-schema.json
slug: snowflake-warehouse
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Snowflake Warehouse
---
