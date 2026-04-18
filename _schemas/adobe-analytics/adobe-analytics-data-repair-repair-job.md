---
description: Status and details of a data repair job
layout: schema
name: RepairJob
properties_list:
- description: Unique job identifier
  name: jobId
  type: integer
- description: The report suite being repaired
  name: reportSuiteId
  type: string
- description: Start of the repair date range
  name: dateRangeStart
  type: string
- description: End of the repair date range
  name: dateRangeEnd
  type: string
- description: Current status of the repair job
  name: status
  type: string
- description: Job completion percentage (0-100)
  name: progress
  type: integer
- description: Timestamp when the job was created
  name: jobCreateTime
  type: string
- description: Timestamp when the job completed
  name: jobCompleteTime
  type: string
- description: Actual number of server calls processed
  name: serverCalls
  type: integer
- description: Number of data nodes processed
  name: nodesProcessed
  type: integer
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-data-repair-repair-job-schema.json
slug: adobe-analytics-data-repair-repair-job
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: RepairJob
---
