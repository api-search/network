---
description: The response when clearing a range of values in a spreadsheet.
layout: schema
name: ClearValuesResponse
properties_list:
- description: The spreadsheet the updates were applied to.
  name: spreadsheetId
  type: string
- description: The range (in A1 notation) that was cleared.
  name: clearedRange
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-clear-values-response-schema.json
slug: google-sheets-clear-values-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: ClearValuesResponse
---
