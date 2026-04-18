---
description: Information about which values in a pivot group should be used for sorting.
layout: schema
name: PivotGroupSortValueBucket
properties_list:
- description: The offset in the PivotTable.values list which the values in this grouping should be sorted by.
  name: valuesIndex
  type: integer
- description: Determines the bucket from which values are chosen to sort.
  name: buckets
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-pivot-group-sort-value-bucket-schema.json
slug: google-sheets-pivot-group-sort-value-bucket
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: PivotGroupSortValueBucket
---
