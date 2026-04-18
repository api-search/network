---
description: Properties of a grid.
layout: schema
name: GridProperties
properties_list:
- description: The number of rows in the grid.
  name: rowCount
  type: integer
- description: The number of columns in the grid.
  name: columnCount
  type: integer
- description: The number of rows that are frozen in the grid.
  name: frozenRowCount
  type: integer
- description: The number of columns that are frozen in the grid.
  name: frozenColumnCount
  type: integer
- description: True if the grid is not showing gridlines in the UI.
  name: hideGridlines
  type: boolean
- description: True if the row grouping control toggle is shown after the group.
  name: rowGroupControlAfter
  type: boolean
- description: True if the column grouping control toggle is shown after the group.
  name: columnGroupControlAfter
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-grid-properties-schema.json
slug: google-sheets-grid-properties
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: GridProperties
---
