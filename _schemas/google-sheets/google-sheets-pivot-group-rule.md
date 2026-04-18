---
description: An optional setting on a PivotGroup that defines buckets for the values in the source data column.
layout: schema
name: PivotGroupRule
properties_list:
- description: A ManualRule.
  name: manualRule
  type: object
- description: A HistogramRule.
  name: histogramRule
  type: object
- description: A DateTimeRule.
  name: dateTimeRule
  type: object
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-pivot-group-rule-schema.json
slug: google-sheets-pivot-group-rule
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: PivotGroupRule
---
