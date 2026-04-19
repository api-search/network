---
description: ''
layout: schema
name: Timesheet
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: descriptor
  type: string
- description: ''
  name: periodStartDate
  type: string
- description: ''
  name: periodEndDate
  type: string
- description: ''
  name: totalHours
  type: number
- description: The status of the timesheet (e.g., Draft, Submitted, Approved).
  name: status
  type: string
- description: ''
  name: calculatedEntries
  type: array
provider_name: Workday
provider_slug: workday
schema_file: json-schema/timeTracking-timesheet-schema.json
slug: timeTracking-timesheet
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Timesheet
---
