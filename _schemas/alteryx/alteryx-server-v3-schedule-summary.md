---
description: Summary representation of a schedule
layout: schema
name: ScheduleSummary
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
- description: ID of the schedule owner
  name: ownerId
  type: string
- description: Next scheduled run date and time
  name: runDateTime
  type: string
- description: Time zone for the schedule
  name: timeZone
  type: string
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-schedule-summary-schema.json
slug: alteryx-server-v3-schedule-summary
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: ScheduleSummary
---
