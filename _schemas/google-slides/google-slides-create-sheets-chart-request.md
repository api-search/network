---
description: Creates an embedded Google Sheets chart.
layout: schema
name: CreateSheetsChartRequest
properties_list:
- description: A user-supplied object ID.
  name: objectId
  type: string
- description: The ID of the Google Sheets spreadsheet that contains the chart.
  name: spreadsheetId
  type: string
- description: The ID of the specific chart in the Google Sheets spreadsheet.
  name: chartId
  type: integer
- description: The mode with which the chart is linked to the source spreadsheet.
  name: linkingMode
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-create-sheets-chart-request-schema.json
slug: google-slides-create-sheets-chart-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: CreateSheetsChartRequest
---
