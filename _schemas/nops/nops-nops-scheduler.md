---
description: ''
layout: schema
name: Scheduler
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
- description: Timestamp when the scheduler was created.
  name: created_at
  type: string
provider_name: nOps
provider_slug: nops
schema_file: json-schema/nops-nops-scheduler-schema.json
slug: nops-nops-scheduler
tags:
- Costs
- FinOps
title: Scheduler
---
