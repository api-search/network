---
description: Represents time-off data for a worker in Workday, including time-off requests, entries, balances, and leave of absence records.
layout: schema
name: Time Off
properties_list:
- description: The Workday ID of the time-off record.
  name: id
  type: string
- description: A display descriptor for the time-off record.
  name: descriptor
  type: string
- description: The worker this time-off record belongs to.
  name: worker
  type: object
- description: The type of time off (e.g., Vacation, Sick, Personal).
  name: timeOffType
  type: object
- description: Individual time-off entries (one per day).
  name: timeOffEntries
  type: array
- description: The status of the time-off request.
  name: status
  type: string
- description: The total quantity of time off requested.
  name: totalQuantity
  type: number
- description: The unit of measure for time off (e.g., Hours, Days).
  name: unit
  type: string
- description: A comment or reason for the time-off request.
  name: comment
  type: string
- description: When the time-off request was submitted.
  name: requestedDate
  type: string
- description: Time-off plan balances for the worker.
  name: balances
  type: array
- description: Leave of absence details, if applicable.
  name: leaveOfAbsence
  type: object
- description: A link to the full time-off resource.
  name: href
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/time-off.json
slug: time-off
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Time Off
---
