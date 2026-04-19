---
description: Request body for stopping a running job.
layout: schema
name: JobStopRequest
properties_list:
- description: The resource type identifier. Must be set to "job".
  name: '@type'
  type: string
- description: The ID of the task to stop. Either taskId or taskName must be provided.
  name: taskId
  type: string
- description: The name of the task to stop. Either taskId or taskName must be provided.
  name: taskName
  type: string
- description: The type of the task to stop.
  name: taskType
  type: string
- description: When true, allows the job to finish processing the current row before stopping. When false, stops the job immediately.
  name: cleanStop
  type: boolean
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-job-stop-request-schema.json
slug: informatica-platform-rest-job-stop-request
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: JobStopRequest
---
