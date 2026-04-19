---
description: Schedule definition for a blackout.
layout: schema
name: BlackoutSchedule
properties_list:
- description: Scheduled start time of the blackout.
  name: startTime
  type: string
- description: Scheduled end time of the blackout.
  name: endTime
  type: string
- description: Duration in minutes if no explicit end time is specified.
  name: duration
  type: integer
- description: Time zone for the schedule.
  name: timezone
  type: string
- description: Recurrence frequency for repeating blackouts.
  name: frequency
  type: string
- description: Interval for repeating blackouts (e.g., every 2 weeks).
  name: repeatInterval
  type: integer
- description: Days of the week for weekly recurrence.
  name: daysOfWeek
  type: array
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-blackout-schedule-schema.json
slug: oracle-enterprise-manager-cloud-control-blackout-schedule
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: BlackoutSchedule
---
