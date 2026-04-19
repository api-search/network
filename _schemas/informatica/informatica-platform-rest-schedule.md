---
description: A task execution schedule.
layout: schema
name: Schedule
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The unique identifier for the schedule.
  name: id
  type: string
- description: The organization ID.
  name: orgId
  type: string
- description: The name of the schedule.
  name: name
  type: string
- description: A description of the schedule.
  name: description
  type: string
- description: The time the schedule was created.
  name: createTime
  type: string
- description: The time the schedule was last updated.
  name: updateTime
  type: string
- description: The user who created the schedule.
  name: createdBy
  type: string
- description: The user who last updated the schedule.
  name: updatedBy
  type: string
- description: The scheduled start time.
  name: startTime
  type: string
- description: The scheduled end time.
  name: endTime
  type: string
- description: The recurrence interval (e.g., None, Daily, Weekly, Monthly).
  name: interval
  type: string
- description: How often the schedule repeats within the interval.
  name: frequency
  type: integer
- description: The time zone for the schedule.
  name: timezone
  type: string
- description: The start of the time range within each day.
  name: rangeStartTime
  type: string
- description: The end of the time range within each day.
  name: rangeEndTime
  type: string
- description: The day(s) of the week for weekly schedules (e.g., Mon, Tue, Wed).
  name: dayOfWeek
  type: string
- description: The day of the month for monthly schedules.
  name: dayOfMonth
  type: integer
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-schedule-schema.json
slug: informatica-platform-rest-schedule
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: Schedule
---
