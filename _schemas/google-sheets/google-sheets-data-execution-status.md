---
description: The data execution status.
layout: schema
name: DataExecutionStatus
properties_list:
- description: The state of the data execution.
  name: state
  type: string
- description: The error code.
  name: errorCode
  type: string
- description: The error message, which may be empty.
  name: errorMessage
  type: string
- description: Gets the time the data last successfully refreshed.
  name: lastRefreshTime
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-data-execution-status-schema.json
slug: google-sheets-data-execution-status
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DataExecutionStatus
---
