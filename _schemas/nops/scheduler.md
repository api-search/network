---
description: A Scheduler automates resource management tasks such as starting and stopping non-production workloads on a defined schedule to reduce costs.
layout: schema
name: nOps Scheduler
properties_list:
- description: The unique identifier of the scheduler.
  name: id
  type: integer
- description: Name of the scheduler.
  name: name
  type: string
- description: Whether the scheduler is currently enabled.
  name: enabled
  type: boolean
- description: The associated nOps AWS Project ID.
  name: project_id
  type: integer
- description: Schedule configuration defining when the scheduler runs.
  name: schedule
  type: object
- description: List of resources managed by this scheduler.
  name: resources
  type: array
- description: Timestamp when the scheduler was created.
  name: created_at
  type: string
provider_name: nOps
provider_slug: nops
schema_file: json-schema/scheduler.json
slug: scheduler
tags:
- Costs
- FinOps
title: nOps Scheduler
---
