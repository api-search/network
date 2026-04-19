---
description: Provides details of a single job.
layout: schema
name: JobResponse
properties_list:
- description: ''
  name: jobId
  type: integer
- description: ''
  name: status
  type: object
- description: ''
  name: jobType
  type: object
- description: ''
  name: startTime
  type: string
- description: ''
  name: connectionId
  type: string
- description: ''
  name: lastUpdatedAt
  type: string
- description: Duration of a sync in ISO_8601 format
  name: duration
  type: string
- description: ''
  name: bytesSynced
  type: integer
- description: ''
  name: rowsSynced
  type: integer
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-job-response-schema.json
slug: airbyte-job-response
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: JobResponse
---
