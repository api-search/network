---
description: ''
layout: schema
name: BaseLanguage
properties_list:
- description: Packages to include with the function/procedure
  name: packages
  type: array
- description: List of imports
  name: imports
  type: array
- description: Fully qualified method name including the package and the class
  name: handler
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/user-defined-function-base-language-schema.json
slug: user-defined-function-base-language
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: BaseLanguage
---
