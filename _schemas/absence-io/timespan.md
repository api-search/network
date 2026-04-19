---
description: A working time configuration defining work hours and schedule.
layout: schema
name: Timespan
properties_list:
- description: Unique identifier of the timespan.
  name: _id
  type: string
- description: Name of the working time configuration.
  name: name
  type: string
- description: Number of working hours per day.
  name: hoursPerDay
  type: number
- description: Number of working days per week.
  name: daysPerWeek
  type: integer
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/timespan-schema.json
slug: timespan
tags:
- Absences
- Employees
- Leave Management
- HR
title: Timespan
---
