---
description: ''
layout: schema
name: DataChangeTask
properties_list:
- description: The Workday ID of the data change task.
  name: id
  type: string
- description: ''
  name: descriptor
  type: string
- description: ''
  name: name
  type: string
- description: The status of the task (e.g., New, Processing, Complete, Error).
  name: status
  type: object
- description: The operation type (e.g., FullReplace, Append).
  name: operation
  type: object
- description: ''
  name: createdOn
  type: string
- description: ''
  name: completedOn
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/prismAnalytics-data-change-task-schema.json
slug: prismAnalytics-data-change-task
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: DataChangeTask
---
