---
description: Data in the grid, as well as metadata about the dimensions.
layout: schema
name: GridData
properties_list:
- description: The first row this GridData refers to, zero-based.
  name: startRow
  type: integer
- description: The first column this GridData refers to, zero-based.
  name: startColumn
  type: integer
- description: The data in the grid, one entry per row, starting with the row in startRow.
  name: rowData
  type: array
- description: Metadata about the requested rows in the grid, starting with the row in startRow.
  name: rowMetadata
  type: array
- description: Metadata about the requested columns in the grid, starting with the column in startColumn.
  name: columnMetadata
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-grid-data-schema.json
slug: google-sheets-grid-data
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: GridData
---
