---
description: A snowflake UDF
layout: schema
name: UserDefinedFunction
properties_list:
- description: The name of the UDF
  name: name
  type: string
- description: Specifies whether the UDF is temporary or not
  name: is_temporary
  type: boolean
- description: Specifies whether the UDF is an aggregate function. Applicable only for Python language type
  name: is_aggregate
  type: boolean
- description: Indicates whether the function is memoizable. Applicable only for Python language type.
  name: is_memoizable
  type: boolean
- description: True if the UDF is a table function; false otherwise.
  name: is_table_function
  type: boolean
- description: True if the UDF is valid for clustering; false otherwise.
  name: valid_for_clustering
  type: boolean
- description: Specifies whether the function/procedure is secure or not
  name: is_secure
  type: boolean
- description: List of arguments for the function/procedure
  name: arguments
  type: array
- description: Specifies a comment for the function/procedure
  name: comment
  type: string
- description: Function/procedure definition
  name: body
  type: string
- description: The date and time when the function/procedure was created
  name: created_on
  type: string
- description: The name of the schema in which the function/procedure exists.
  name: schema_name
  type: string
- description: The name of the database in which the function/procedure exists.
  name: database_name
  type: string
- description: The minimum number of arguments
  name: min_num_arguments
  type: integer
- description: The maximum number of arguments
  name: max_num_arguments
  type: integer
- description: Role that owns the function/procedure
  name: owner
  type: string
- description: The type of role that owns the function/procedure
  name: owner_role_type
  type: string
- description: If the function/procedure is built-in or not (user-defined)
  name: is_builtin
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/user-defined-function-user-defined-function-schema.json
slug: user-defined-function-user-defined-function
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: UserDefinedFunction
---
