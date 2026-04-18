---
description: Properties of a spreadsheet.
layout: schema
name: SpreadsheetProperties
properties_list:
- description: The title of the spreadsheet.
  name: title
  type: string
- description: 'The locale of the spreadsheet in one of the following formats: an ISO 639-1 language code, an ISO 639-2 language code, or a combination of the ISO language code and country code (e.g. en, eng, en_US).'
  name: locale
  type: string
- description: The amount of time to wait before volatile functions are recalculated.
  name: autoRecalc
  type: string
- description: The time zone of the spreadsheet in CLDR format (e.g. America/New_York).
  name: timeZone
  type: string
- description: Whether to allow external URL access for image and import functions.
  name: importFunctionsExternalUrlAccessAllowed
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-spreadsheet-properties-schema.json
slug: google-sheets-spreadsheet-properties
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: SpreadsheetProperties
---
