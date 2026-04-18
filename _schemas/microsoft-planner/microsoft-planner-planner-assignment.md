---
description: Represents the assignment of a task to a user
layout: schema
name: PlannerAssignment
properties_list:
- description: ''
  name: '@odata.type'
  type: string
- description: The time at which the task was assigned
  name: assignedDateTime
  type: string
- description: Hint used to order assignees in a task. The format is defined in the Planner order hints documentation.
  name: orderHint
  type: string
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-assignment-schema.json
slug: microsoft-planner-planner-assignment
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerAssignment
---
