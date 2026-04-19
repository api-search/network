---
description: Schedule configuration for automated report generation and delivery.
layout: schema
name: ReportSchedule
properties_list:
- description: Whether the schedule is active.
  name: active
  type: boolean
- description: The interval at which the report is run. Acceptable values are DAILY, WEEKLY, MONTHLY, or QUARTERLY.
  name: repeats
  type: string
- description: Defines every how many days, weeks, or months the report should be run.
  name: every
  type: integer
- description: Start date of the scheduled reports.
  name: startDate
  type: string
- description: The expiration date when the scheduled report stops running.
  name: expirationDate
  type: string
- description: Enum to define for MONTHLY and QUARTERLY schedules whether reports should be repeated on the same day of the month or the same day of the week.
  name: runsOnDayOfMonth
  type: string
- description: The timezone for the report schedule.
  name: timezone
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-report-schedule-schema.json
slug: google-campaign-manager-report-schedule
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: ReportSchedule
---
