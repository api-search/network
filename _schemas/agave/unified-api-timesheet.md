---
description: An employee timesheet entry.
layout: schema
name: Timesheet
properties_list:
- description: Timesheet identifier.
  name: id
  type: string
- description: Employee identifier.
  name: employee_id
  type: string
- description: Associated project identifier.
  name: project_id
  type: string
- description: Associated cost code.
  name: cost_code_id
  type: string
- description: Timesheet date.
  name: date
  type: string
- description: Regular hours worked.
  name: regular_hours
  type: number
- description: Overtime hours worked.
  name: overtime_hours
  type: number
- description: Hourly pay rate in USD.
  name: pay_rate
  type: number
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-timesheet-schema.json
slug: unified-api-timesheet
tags:
- Accounting
- Construction
- Integration
title: Timesheet
---
