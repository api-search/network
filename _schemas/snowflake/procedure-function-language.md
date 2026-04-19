---
description: ''
layout: schema
name: FunctionLanguage
properties_list:
- description: 'Language that the function/procedure is written in. Possible values include: JAVA, JAVASCRIPT, PYTHON, SCALA, SQL'
  name: language
  type: string
- description: Decide if the function/procedure can receive null input
  name: called_on_null_input
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/procedure-function-language-schema.json
slug: procedure-function-language
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: FunctionLanguage
---
