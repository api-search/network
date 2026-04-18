---
description: Schedule for refreshing a data source.
layout: schema
name: DataSourceRefreshSchedule
properties_list:
- description: True if the refresh schedule is enabled.
  name: enabled
  type: boolean
- description: The scope of the refresh.
  name: refreshScope
  type: string
- description: Output only. The time interval of the next run.
  name: nextRun
  type: object
- description: Daily refresh schedule.
  name: dailySchedule
  type: object
- description: Weekly refresh schedule.
  name: weeklySchedule
  type: object
- description: Monthly refresh schedule.
  name: monthlySchedule
  type: object
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-data-source-refresh-schedule-schema.json
slug: google-sheets-data-source-refresh-schedule
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DataSourceRefreshSchedule
---
