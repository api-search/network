---
description: Request body for creating a new schedule.
layout: schema
name: ScheduleCreateRequest
properties_list:
- description: ''
  name: '@type'
  type: string
- description: The name for the new schedule.
  name: name
  type: string
- description: A description of the schedule.
  name: description
  type: string
- description: The scheduled start time.
  name: startTime
  type: string
- description: The scheduled end time.
  name: endTime
  type: string
- description: The recurrence interval.
  name: interval
  type: string
- description: The repeat frequency.
  name: frequency
  type: integer
- description: The time zone.
  name: timezone
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-schedule-create-request-schema.json
slug: informatica-platform-rest-schedule-create-request
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
title: ScheduleCreateRequest
---
