---
description: Summary representation of an execution job
layout: schema
name: JobSummary
properties_list:
- description: Unique job identifier
  name: id
  type: string
- description: Date the job was created
  name: createDate
  type: string
- description: Current job status
  name: status
  type: string
- description: Job priority
  name: priority
  type: string
- description: Worker tag for execution routing
  name: workerTag
  type: string
- description: Whether the job runs with AMP engine
  name: runWithE2
  type: boolean
provider_name: Alteryx
provider_slug: alteryx
schema_file: json-schema/alteryx-server-v3-job-summary-schema.json
slug: alteryx-server-v3-job-summary
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
title: JobSummary
---
