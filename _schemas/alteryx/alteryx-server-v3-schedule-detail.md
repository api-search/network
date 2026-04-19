---
description: Detailed representation of a schedule
layout: schema
name: ScheduleDetail
properties_list:
- description: Unique schedule identifier
  name: id
  type: string
- description: Name of the schedule
  name: name
  type: string
- description: ID of the associated workflow
  name: workflowId
  type: string
- description: Specific workflow version ID
  name: versionId
  type: string
- description: ID of the schedule owner
  name: ownerId
  type: string
- description: Next scheduled run date and time
  name: runDateTime
  type: string
- description: Comments about the schedule
  name: comment
  type: string
- description: Whether the schedule is active
  name: enabled
  type: boolean
- description: Execution priority
  name: priority
  type: string
- description: Worker tag for execution routing
  name: workerTag
  type: string
- description: Current status of the schedule
  name: status
  type: string
- description: Credential used for execution
  name: credentialId
  type: string
- description: When the schedule was created
  name: creationTime
  type: string
- description: When the schedule last executed
  name: lastRunTime
  type: string
- description: Current state of the schedule
  name: state
  type: string
- description: Total number of times the schedule has executed
  name: runCount
  type: integer
- description: Human-readable frequency description
  name: frequency
  type: string
- description: Last error message if any
  name: lastError
  type: string
- description: Name of the worker node
  name: cpuName
  type: string
- description: ID of the user who last modified the schedule
  name: lastModifiedId
  type: string
- description: Date of last modification
  name: lastModifiedDate
  type: string
- description: Whether the current user can edit this schedule
  name: canEdit
  type: boolean
- description: Time zone for the schedule
  name: timeZone
  type: string
- description: Analytic app question values
  name: questions
  type: array
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-schedule-detail-schema.json
slug: alteryx-server-v3-schedule-detail
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: ScheduleDetail
---
