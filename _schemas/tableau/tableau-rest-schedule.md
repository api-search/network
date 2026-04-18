---
description: ''
layout: schema
name: Schedule
properties_list:
- description: The unique identifier for the schedule.
  name: id
  type: string
- description: The name of the schedule.
  name: name
  type: string
- description: Whether the schedule is active or suspended.
  name: state
  type: string
- description: The priority of the schedule (1-100). Lower numbers indicate higher priority.
  name: priority
  type: integer
- description: The date and time the schedule was created.
  name: createdAt
  type: string
- description: The date and time the schedule was last updated.
  name: updatedAt
  type: string
- description: The type of the schedule.
  name: type
  type: string
- description: How frequently the schedule runs.
  name: frequency
  type: string
- description: The next scheduled run time.
  name: nextRunAt
  type: string
- description: The time when the schedule ends.
  name: endScheduleAt
  type: string
- description: ''
  name: frequencyDetails
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-schedule-schema.json
slug: tableau-rest-schedule
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Schedule
---
