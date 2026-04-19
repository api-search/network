---
description: ''
layout: schema
name: PythonFunction
properties_list:
- description: List of external access integrations attached to this function/procedure
  name: external_access_integrations
  type: array
- description: Secrets to be used with this function/procedure for external access
  name: secrets
  type: object
- description: 'Specifies the Python version to use. The supported versions of Python are: * 3.8 * 3.9 * 3.10 * 3.11'
  name: runtime_version
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/user-defined-function-python-function-schema.json
slug: user-defined-function-python-function
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: PythonFunction
---
