---
description: A Snowflake procedure
layout: schema
name: Procedure
properties_list:
- description: Name of the procedure
  name: name
  type: string
- description: What permissions should the procedure execution be called with
  name: execute_as
  type: string
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
schema_file: json-schema/procedure-procedure-schema.json
slug: procedure-procedure
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Procedure
---
