---
description: A Snowflake function
layout: schema
name: Function
properties_list:
- description: ''
  name: function_type
  type: string
- description: Specifies the name for the function, must be unique for the schema in which the function is created
  name: name
  type: string
- description: ''
  name: arguments
  type: array
- description: Specifies the type for the function return value.
  name: returns
  type: string
- description: Specifies the max rows for batch operation.
  name: max_batch_rows
  type: integer
- description: Date and time when the function was created.
  name: created_on
  type: string
- description: Function's arguments.
  name: signature
  type: string
- description: Function's language.
  name: language
  type: string
- description: Function's body.
  name: body
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/function-function-schema.json
slug: function-function
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Function
---
