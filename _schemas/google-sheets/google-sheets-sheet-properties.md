---
description: Properties of a sheet.
layout: schema
name: SheetProperties
properties_list:
- description: The ID of the sheet. Must be non-negative. This field cannot be changed once set.
  name: sheetId
  type: integer
- description: The name of the sheet.
  name: title
  type: string
- description: The index of the sheet within the spreadsheet.
  name: index
  type: integer
- description: The type of sheet.
  name: sheetType
  type: string
- description: True if the sheet is hidden in the UI, false if visible.
  name: hidden
  type: boolean
- description: True if the sheet is an RTL sheet instead of an LTR sheet.
  name: rightToLeft
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-sheet-properties-schema.json
slug: google-sheets-sheet-properties
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: SheetProperties
---
