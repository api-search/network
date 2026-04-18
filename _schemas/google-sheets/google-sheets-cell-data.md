---
description: Data about a specific cell.
layout: schema
name: CellData
properties_list:
- description: The formatted value of the cell. This is the value as it is shown to the user.
  name: formattedValue
  type: string
- description: A hyperlink this cell points to, if any.
  name: hyperlink
  type: string
- description: Any note on the cell.
  name: note
  type: string
- description: Runs of rich text applied to subsections of the cell.
  name: textFormatRuns
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-cell-data-schema.json
slug: google-sheets-cell-data
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: CellData
---
