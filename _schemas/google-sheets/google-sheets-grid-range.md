---
description: A range on a sheet. All indexes are zero-based.
layout: schema
name: GridRange
properties_list:
- description: The sheet this range is on.
  name: sheetId
  type: integer
- description: The start row (inclusive) of the range, or not set if unbounded.
  name: startRowIndex
  type: integer
- description: The end row (exclusive) of the range, or not set if unbounded.
  name: endRowIndex
  type: integer
- description: The start column (inclusive) of the range, or not set if unbounded.
  name: startColumnIndex
  type: integer
- description: The end column (exclusive) of the range, or not set if unbounded.
  name: endColumnIndex
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-grid-range-schema.json
slug: google-sheets-grid-range
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: GridRange
---
