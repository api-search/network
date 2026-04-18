---
description: A sheet in a spreadsheet.
layout: schema
name: Sheet
properties_list:
- description: Data in the grid, if this is a grid sheet.
  name: data
  type: array
- description: The ranges that are merged together.
  name: merges
  type: array
- description: The conditional format rules in this sheet.
  name: conditionalFormats
  type: array
- description: The filter views in this sheet.
  name: filterViews
  type: array
- description: The protected ranges in this sheet.
  name: protectedRanges
  type: array
- description: The specifications of every chart on this sheet.
  name: charts
  type: array
- description: The banded (alternating colors) ranges on this sheet.
  name: bandedRanges
  type: array
- description: The slicers on this sheet.
  name: slicers
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-sheet-schema.json
slug: google-sheets-sheet
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: Sheet
---
