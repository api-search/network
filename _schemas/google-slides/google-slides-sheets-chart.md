---
description: A PageElement kind representing a linked chart embedded from Google Sheets.
layout: schema
name: SheetsChart
properties_list:
- description: The ID of the Google Sheets spreadsheet that contains the source chart.
  name: spreadsheetId
  type: string
- description: The ID of the specific chart in the Google Sheets spreadsheet.
  name: chartId
  type: integer
- description: The URL of an image of the embedded chart, with a default lifetime of 30 minutes.
  name: contentUrl
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-sheets-chart-schema.json
slug: google-slides-sheets-chart
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: SheetsChart
---
