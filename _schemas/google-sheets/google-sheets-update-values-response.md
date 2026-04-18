---
description: The response when updating a range of values in a spreadsheet.
layout: schema
name: UpdateValuesResponse
properties_list:
- description: The spreadsheet the updates were applied to.
  name: spreadsheetId
  type: string
- description: The range (in A1 notation) that updates were applied to.
  name: updatedRange
  type: string
- description: The number of rows where at least one cell in the row was updated.
  name: updatedRows
  type: integer
- description: The number of columns where at least one cell in the column was updated.
  name: updatedColumns
  type: integer
- description: The number of cells updated.
  name: updatedCells
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-update-values-response-schema.json
slug: google-sheets-update-values-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: UpdateValuesResponse
---
