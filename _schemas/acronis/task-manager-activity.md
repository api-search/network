---
description: A subordinate activity within a task
layout: schema
name: Activity
properties_list:
- description: Activity unique identifier
  name: id
  type: string
- description: Activity type
  name: type
  type: string
- description: ''
  name: state
  type: string
- description: ''
  name: result_code
  type: string
- description: Parent activity UUID if nested
  name: parent_activity_id
  type: string
- description: Parent task identifier
  name: task_id
  type: string
- description: Whether activity can be requeued on failure
  name: sustainable
  type: boolean
- description: ''
  name: createdAt
  type: string
- description: ''
  name: startedAt
  type: string
- description: ''
  name: completedAt
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/task-manager-activity-schema.json
slug: task-manager-activity
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Activity
---
