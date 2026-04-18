---
description: A location where metadata may be associated in a spreadsheet.
layout: schema
name: DeveloperMetadataLocation
properties_list:
- description: The type of location this object represents.
  name: locationType
  type: string
- description: True when metadata is associated with an entire spreadsheet.
  name: spreadsheet
  type: boolean
- description: The ID of the sheet when metadata is associated with an entire sheet.
  name: sheetId
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-developer-metadata-location-schema.json
slug: google-sheets-developer-metadata-location
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DeveloperMetadataLocation
---
