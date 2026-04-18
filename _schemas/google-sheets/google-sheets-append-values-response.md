---
description: The response when updating a range of values by appending.
layout: schema
name: AppendValuesResponse
properties_list:
- description: The spreadsheet the updates were applied to.
  name: spreadsheetId
  type: string
- description: The range (in A1 notation) of the table that values are being appended to.
  name: tableRange
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-append-values-response-schema.json
slug: google-sheets-append-values-response
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: AppendValuesResponse
---
