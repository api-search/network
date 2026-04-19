---
description: Snowflake parameter defined at the system, account, user, session, or object level.
layout: schema
name: Parameter
properties_list:
- description: Parameter name.
  name: name
  type: string
- description: Parameter value.
  name: value
  type: string
- description: Default parameter value.
  name: defaultValue
  type: string
- description: Data type of the parameter value. Either BOOLEAN, NUMBER, FLOAT, or STRING.
  name: dataType
  type: string
- description: Level at which parameter is defined.
  name: level
  type: string
- description: Parameter description.
  name: description
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/common-parameter-schema.json
slug: common-parameter
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Parameter
---
