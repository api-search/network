---
description: Async job status response
layout: schema
name: JobResponse
properties_list:
- description: Unique identifier for the async job
  name: jobId
  type: string
- description: Current status of the job
  name: status
  type: string
- description: Result data after successful job completion
  name: result
  type: object
- description: When the job was created
  name: createdAt
  type: string
- description: When the job completed (null if still pending)
  name: completedAt
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-claims-job_response-schema.json
slug: trade-claims-job_response
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: JobResponse
---
