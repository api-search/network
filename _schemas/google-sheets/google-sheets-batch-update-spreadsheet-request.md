---
description: The request for updating any aspect of a spreadsheet.
layout: schema
name: BatchUpdateSpreadsheetRequest
properties_list:
- description: A list of updates to apply to the spreadsheet.
  name: requests
  type: array
- description: Determines if the update response should include the spreadsheet resource.
  name: includeSpreadsheetInResponse
  type: boolean
- description: Limits the ranges included in the response spreadsheet.
  name: responseRanges
  type: array
- description: True if grid data should be returned.
  name: responseIncludeGridData
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-batch-update-spreadsheet-request-schema.json
slug: google-sheets-batch-update-spreadsheet-request
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BatchUpdateSpreadsheetRequest
---
