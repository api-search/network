---
description: A Google Sheets spreadsheet resource.
layout: schema
name: Spreadsheet
properties_list:
- description: The ID of the spreadsheet. Read-only.
  name: spreadsheetId
  type: string
- description: The sheets that are part of a spreadsheet.
  name: sheets
  type: array
- description: The named ranges defined in a spreadsheet.
  name: namedRanges
  type: array
- description: The URL of the spreadsheet. Read-only.
  name: spreadsheetUrl
  type: string
- description: The developer metadata associated with a spreadsheet.
  name: developerMetadata
  type: array
- description: A list of external data sources connected to the spreadsheet.
  name: dataSources
  type: array
- description: Output only. A list of data source refresh schedules.
  name: dataSourceSchedules
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-spreadsheet-schema.json
slug: google-sheets-spreadsheet
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: Spreadsheet
---
