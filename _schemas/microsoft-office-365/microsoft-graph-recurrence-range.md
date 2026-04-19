---
description: Describes a date range over which a recurring event repeats.
layout: schema
name: RecurrenceRange
properties_list:
- description: The recurrence range type.
  name: type
  type: string
- description: The start date of the series (first occurrence).
  name: startDate
  type: string
- description: The date to stop applying the recurrence pattern.
  name: endDate
  type: string
- description: The number of times to repeat the event.
  name: numberOfOccurrences
  type: integer
- description: Time zone for the startDate and endDate properties.
  name: recurrenceTimeZone
  type: string
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-recurrence-range-schema.json
slug: microsoft-graph-recurrence-range
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: RecurrenceRange
---
