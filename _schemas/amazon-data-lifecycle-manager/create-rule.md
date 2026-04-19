---
description: Specifies when and how to create snapshots.
layout: schema
name: Create Rule
properties_list:
- description: The interval between snapshots
  name: Interval
  type: integer
- description: ''
  name: IntervalUnit
  type: string
- description: ''
  name: Times
  type: array
- description: ''
  name: CronExpression
  type: string
provider_name: Amazon Data Lifecycle Manager
provider_slug: amazon-data-lifecycle-manager
schema_file: json-schema/create-rule-schema.json
slug: create-rule
tags:
- AWS
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
title: Create Rule
---
