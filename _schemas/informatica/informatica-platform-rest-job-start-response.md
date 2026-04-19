---
description: Response returned when a job is successfully started.
layout: schema
name: JobStartResponse
properties_list:
- description: The ID of the task that was started.
  name: taskId
  type: string
- description: The type of the task.
  name: taskType
  type: string
- description: The unique run ID for this job execution. Use this ID to track job status.
  name: runId
  type: integer
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-job-start-response-schema.json
slug: informatica-platform-rest-job-start-response
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
title: JobStartResponse
---
