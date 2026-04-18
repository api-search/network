---
description: A rule describing a conditional format.
layout: schema
name: ConditionalFormatRule
properties_list:
- description: The ranges that are formatted if the condition is true.
  name: ranges
  type: array
- description: The formatting is either on or off according to the rule.
  name: booleanRule
  type: object
- description: The formatting will vary based on the gradients in the rule.
  name: gradientRule
  type: object
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-conditional-format-rule-schema.json
slug: google-sheets-conditional-format-rule
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: ConditionalFormatRule
---
