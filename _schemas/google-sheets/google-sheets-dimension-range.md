---
description: A range along a single dimension on a sheet.
layout: schema
name: DimensionRange
properties_list:
- description: The sheet this span is on.
  name: sheetId
  type: integer
- description: The start (inclusive) of the span.
  name: startIndex
  type: integer
- description: The end (exclusive) of the span.
  name: endIndex
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-dimension-range-schema.json
slug: google-sheets-dimension-range
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DimensionRange
---
