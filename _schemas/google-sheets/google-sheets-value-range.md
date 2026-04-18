---
description: Data within a range of the spreadsheet.
layout: schema
name: ValueRange
properties_list:
- description: The range the values cover, in A1 notation. For output, this range indicates the entire requested range, even though the values response will include only the non-empty rows and columns.
  name: range
  type: string
- description: The data that was read or to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension.
  name: values
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-value-range-schema.json
slug: google-sheets-value-range
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: ValueRange
---
