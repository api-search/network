---
description: A bind variable value with its Snowflake data type.
layout: schema
name: BindVariable
properties_list:
- description: The Snowflake data type of the bind variable (e.g. FIXED, TEXT, BOOLEAN, DATE, TIMESTAMP_LTZ, TIMESTAMP_NTZ, TIMESTAMP_TZ).
  name: type
  type: string
- description: The value of the bind variable as a string.
  name: value
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-bind-variable-schema.json
slug: snowflake-sql-rest-bind-variable
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: BindVariable
---
