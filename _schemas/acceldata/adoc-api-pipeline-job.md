---
description: A monitored data pipeline job execution
layout: schema
name: PipelineJob
properties_list:
- description: Job execution identifier
  name: id
  type: string
- description: Pipeline job name
  name: name
  type: string
- description: Platform running the job
  name: platform
  type: string
- description: Job execution status
  name: status
  type: string
- description: Job start time
  name: startTime
  type: string
- description: Job end time
  name: endTime
  type: string
- description: Job duration in seconds
  name: durationSeconds
  type: integer
- description: SLA compliance status
  name: slaStatus
  type: string
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-pipeline-job-schema.json
slug: adoc-api-pipeline-job
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: PipelineJob
---
