---
consumed_apis:
- workday-time-tracking
- workday-absence
description: Unified time and absence management combining Time Tracking and Absence Management APIs for HR operations to manage timesheets, time-off requests, and leave balances.
layout: capability
name: Workday Time and Absence
operations:
- description: List time entries
  method: GET
  name: list-time-entries
  path: /v1/time-entries
- description: List time-off balances
  method: GET
  name: list-balances
  path: /v1/time-off-balances
personas: []
provider_name: Workday
provider_slug: workday
search_terms:
- list time entries
- create a time clock event
- time tracking
- list leaves of absence
- list time-off balances
- absence get balances
- list timesheets
- absence list time off entries
- financial management
- list balances
- get time-off balances for a worker
- absence request time off
- absence management
- submit a leave of absence request
- list time clock events
- workday
- time list clock events
- saas
- time request entry
- list time-off entries
- enterprise software
- cloud computing
- absence list leaves
- time create clock event
- hcm
- time list entries
- absence request leave
- time entries
- submit a time entry request
- get eligible absence types for a worker
- time-off balances
- submit a time-off request
- absence get eligible types
- time list timesheets
slug: time-and-absence
tags:
- Workday
- Time Tracking
- Absence Management
tools:
- description: List time clock events
  hints:
    readOnly: true
  name: time-list-clock-events
- description: Create a time clock event
  hints:
    readOnly: false
  name: time-create-clock-event
- description: List time entries
  hints:
    readOnly: true
  name: time-list-entries
- description: List timesheets
  hints:
    readOnly: true
  name: time-list-timesheets
- description: Submit a time entry request
  hints:
    readOnly: false
  name: time-request-entry
- description: Get eligible absence types for a worker
  hints:
    readOnly: true
  name: absence-get-eligible-types
- description: Submit a time-off request
  hints:
    readOnly: false
  name: absence-request-time-off
- description: List time-off entries
  hints:
    readOnly: true
  name: absence-list-time-off-entries
- description: Get time-off balances for a worker
  hints:
    readOnly: true
  name: absence-get-balances
- description: List leaves of absence
  hints:
    readOnly: true
  name: absence-list-leaves
- description: Submit a leave of absence request
  hints:
    readOnly: false
  name: absence-request-leave
---
