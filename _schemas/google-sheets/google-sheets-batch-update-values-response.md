---
description: The response when updating a range of values in a spreadsheet.
layout: schema
name: BatchUpdateValuesResponse
properties_list:
- description: The spreadsheet the updates were applied to.
  name: spreadsheetId
  type: string
- description: The total number of rows where at least one cell in the row was updated.
  name: totalUpdatedRows
  type: integer
- description: The total number of columns where at least one cell in the column was updated.
  name: totalUpdatedColumns
  type: integer
- description: The total number of cells updated.
  name: totalUpdatedCells
  type: integer
- description: The total number of sheets where at least one cell in the sheet was updated.
  name: totalUpdatedSheets
  type: integer
- description: One UpdateValuesResponse per requested range, in the same order as the requests appeared.
  name: responses
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-batch-update-values-response-schema.json
slug: google-sheets-batch-update-values-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BatchUpdateValuesResponse
---
