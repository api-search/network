---
description: ''
layout: schema
name: SchedulerCreateRequest
properties_list:
- description: Name of the scheduler.
  name: name
  type: string
- description: The nOps AWS Project ID to associate with.
  name: project_id
  type: integer
- description: Schedule configuration for the scheduler.
  name: schedule
  type: object
- description: List of resources to manage with this scheduler.
  name: resources
  type: array
provider_name: nOps
provider_slug: nops
schema_file: json-schema/nops-nops-scheduler-create-request-schema.json
slug: nops-nops-scheduler-create-request
tags:
- Costs
- FinOps
title: SchedulerCreateRequest
---
