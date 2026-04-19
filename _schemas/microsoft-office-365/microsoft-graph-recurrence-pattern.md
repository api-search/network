---
description: Describes the frequency by which a recurring event repeats.
layout: schema
name: RecurrencePattern
properties_list:
- description: The recurrence pattern type.
  name: type
  type: string
- description: The number of units between occurrences, where units can be in days, weeks, months, or years.
  name: interval
  type: integer
- description: A collection of the days of the week on which the event occurs.
  name: daysOfWeek
  type: array
- description: The day of the month on which the event occurs.
  name: dayOfMonth
  type: integer
- description: The month in which the event occurs (1-12).
  name: month
  type: integer
- description: The first day of the week.
  name: firstDayOfWeek
  type: string
- description: The week index for relative monthly and yearly patterns.
  name: index
  type: string
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-recurrence-pattern-schema.json
slug: microsoft-graph-recurrence-pattern
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: RecurrencePattern
---
