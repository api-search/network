---
description: Represents a bucket (custom column) for tasks in a plan in Microsoft 365. It is contained in a plannerPlan and can have a collection of plannerTasks.
layout: schema
name: PlannerBucket
properties_list:
- description: The ETag of the resource, used for concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier for the bucket. 28 characters long and case-sensitive.
  name: id
  type: string
- description: Name of the bucket
  name: name
  type: string
- description: Plan ID to which the bucket belongs
  name: planId
  type: string
- description: Hint used to order buckets in a list view
  name: orderHint
  type: string
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-bucket-schema.json
slug: microsoft-planner-planner-bucket
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerBucket
---
