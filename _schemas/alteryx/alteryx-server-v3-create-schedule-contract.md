---
description: Contract for creating a new schedule
layout: schema
name: CreateScheduleContract
properties_list:
- description: ID of the workflow to schedule
  name: workflowId
  type: string
- description: Name of the schedule
  name: name
  type: string
- description: Comments about the schedule
  name: comment
  type: string
- description: Execution priority
  name: priority
  type: string
- description: Worker tag for execution routing
  name: workerTag
  type: string
- description: Credential to use for execution
  name: credentialId
  type: string
- description: Time zone for the schedule (defaults to UTC-0)
  name: timeZone
  type: string
- description: Analytic app question values
  name: questions
  type: array
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-create-schedule-contract-schema.json
slug: alteryx-server-v3-create-schedule-contract
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: CreateScheduleContract
---
