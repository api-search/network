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
- description: 'Specifies the behavior of the UDF when returning results. This Field is deprecated for Procedure. If true, UDF might return different values for different rows, even for the same input. This field is '
  name: is_volatile
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/user-defined-function-function-language-schema.json
slug: user-defined-function-function-language
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: FunctionLanguage
---
