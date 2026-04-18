---
description: The definition of how a value in a pivot table should be calculated.
layout: schema
name: PivotValue
properties_list:
- description: A function to summarize the value.
  name: summarizeFunction
  type: string
- description: A name to use for the value.
  name: name
  type: string
- description: If specified, indicates that pivot values should be displayed as the result of a calculation with another pivot value.
  name: calculatedDisplayType
  type: string
- description: The column offset of the source range that this value reads from.
  name: sourceColumnOffset
  type: integer
- description: A custom formula to calculate the value.
  name: formula
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-pivot-value-schema.json
slug: google-sheets-pivot-value
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: PivotValue
---
