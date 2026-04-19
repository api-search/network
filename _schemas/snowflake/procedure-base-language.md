---
description: ''
layout: schema
name: BaseLanguage
properties_list:
- description: Runtime version of the function's/procedure's specified language
  name: runtime_version
  type: string
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
schema_file: json-schema/procedure-base-language-schema.json
slug: procedure-base-language
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: BaseLanguage
---
