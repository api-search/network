---
description: A rendering job submitted to a queue in Amazon Deadline Cloud.
layout: schema
name: Job
properties_list:
- description: The unique identifier of the job
  name: jobId
  type: string
- description: ''
  name: queueId
  type: string
- description: ''
  name: farmId
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: lifecycleStatus
  type: string
- description: ''
  name: taskRunStatus
  type: string
- description: ''
  name: priority
  type: integer
- description: ''
  name: createdAt
  type: string
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
schema_file: json-schema/job-schema.json
slug: job
tags:
- AWS
- Compute
- Media
- Rendering
- Visual Effects
title: Job
---
