---
description: Specifies the schedule for creating snapshots.
layout: schema
name: Schedule
properties_list:
- description: The name of the schedule
  name: Name
  type: string
- description: ''
  name: CreateRule
  type: object
- description: ''
  name: RetainRule
  type: object
- description: ''
  name: TagsToAdd
  type: array
- description: ''
  name: CopyTags
  type: boolean
provider_name: Amazon Data Lifecycle Manager
provider_slug: amazon-data-lifecycle-manager
schema_file: json-schema/schedule-schema.json
slug: schedule
tags:
- AWS
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
title: Schedule
---
