---
description: The request for updating more than one range of values in a spreadsheet.
layout: schema
name: BatchUpdateValuesRequest
properties_list:
- description: The new values to apply to the spreadsheet.
  name: data
  type: array
- description: Determines if the update response should include the values of the cells that were updated.
  name: includeValuesInResponse
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-batch-update-values-request-schema.json
slug: google-sheets-batch-update-values-request
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BatchUpdateValuesRequest
---
