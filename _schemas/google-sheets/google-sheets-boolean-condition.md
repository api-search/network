---
description: A condition that can evaluate to true or false.
layout: schema
name: BooleanCondition
properties_list:
- description: The type of condition.
  name: type
  type: string
- description: The values of the condition. The number of supported values depends on the condition type.
  name: values
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-boolean-condition-schema.json
slug: google-sheets-boolean-condition
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BooleanCondition
---
