---
description: ''
layout: schema
name: JavaFunction
properties_list:
- description: List of external access integrations attached to this function/procedure
  name: external_access_integrations
  type: array
- description: Secrets to be used with this function/procedure for external access
  name: secrets
  type: object
- description: Specifies where Snowflake should write the compiled code for inline procedures
  name: target_path
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/procedure-java-function-schema.json
slug: procedure-java-function
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: JavaFunction
---
