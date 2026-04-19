---
description: Provides full details of when the job has been run
layout: schema
name: runsForJob
properties_list:
- description: The date and time the job was finished processing
  name: endTime
  type: string
- description: The ID of the run
  name: id
  type: string
- description: Indicates whether the job was triggered via the PRB API
  name: isApiTriggered
  type: boolean
- description: Number of seconds between startTime and endTime
  name: runDuration
  type: number
- description: The date and time the job started running after being submitted and potentially waiting in any queue
  name: startTime
  type: string
- description: The date and time the job was submitted
  name: submitTime
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-portfolio-reporting-batcher-runs-for-job-schema.json
slug: factset-portfolio-reporting-batcher-runs-for-job
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: runsForJob
---
