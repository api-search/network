---
description: The response when clearing a range of values in a spreadsheet.
layout: schema
name: BatchClearValuesResponse
properties_list:
- description: The spreadsheet the updates were applied to.
  name: spreadsheetId
  type: string
- description: The ranges that were cleared, in A1 notation.
  name: clearedRanges
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-batch-clear-values-response-schema.json
slug: google-sheets-batch-clear-values-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BatchClearValuesResponse
---
