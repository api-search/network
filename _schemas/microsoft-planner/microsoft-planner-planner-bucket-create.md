---
description: Request body for creating a new bucket
layout: schema
name: PlannerBucketCreate
properties_list:
- description: Name of the bucket
  name: name
  type: string
- description: ID of the plan the bucket belongs to
  name: planId
  type: string
- description: Hint used to order the bucket
  name: orderHint
  type: string
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-bucket-create-schema.json
slug: microsoft-planner-planner-bucket-create
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerBucketCreate
---
