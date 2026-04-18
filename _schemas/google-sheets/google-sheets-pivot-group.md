---
description: A single grouping (either row or column) in a pivot table.
layout: schema
name: PivotGroup
properties_list:
- description: The column offset of the source range that this grouping is based on.
  name: sourceColumnOffset
  type: integer
- description: True if the pivot table should include the totals for this grouping.
  name: showTotals
  type: boolean
- description: The order the values in this group should be sorted.
  name: sortOrder
  type: string
- description: True if the headings in this pivot group should be repeated.
  name: repeatHeadings
  type: boolean
- description: The labels to use for the row/column groups which can be customized.
  name: label
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-pivot-group-schema.json
slug: google-sheets-pivot-group
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: PivotGroup
---
