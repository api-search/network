---
description: Information about an external data source in the spreadsheet.
layout: schema
name: DataSource
properties_list:
- description: The spreadsheet-scoped unique ID that identifies the data source.
  name: dataSourceId
  type: string
- description: All calculated columns in the data source.
  name: calculatedColumns
  type: array
- description: The ID of the Sheet connected with the data source.
  name: sheetId
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-data-source-schema.json
slug: google-sheets-data-source
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DataSource
---
