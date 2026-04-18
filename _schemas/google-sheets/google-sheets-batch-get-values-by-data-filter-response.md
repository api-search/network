---
description: The response when retrieving more than one range of values in a spreadsheet selected by DataFilters.
layout: schema
name: BatchGetValuesByDataFilterResponse
properties_list:
- description: The ID of the spreadsheet the data was retrieved from.
  name: spreadsheetId
  type: string
- description: The requested values with the list of data filters that matched them.
  name: valueRanges
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-batch-get-values-by-data-filter-response-schema.json
slug: google-sheets-batch-get-values-by-data-filter-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BatchGetValuesByDataFilterResponse
---
