---
description: A data validation rule.
layout: schema
name: DataValidationRule
properties_list:
- description: A message to show the user when adding data to the cell.
  name: inputMessage
  type: string
- description: True if invalid data should be rejected.
  name: strict
  type: boolean
- description: True if the UI should be customized based on the kind of condition.
  name: showCustomUi
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-data-validation-rule-schema.json
slug: google-sheets-data-validation-rule
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DataValidationRule
---
