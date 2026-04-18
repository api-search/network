---
description: Request body for an enhanced dataset refresh
layout: schema
name: RefreshRequest
properties_list:
- description: The type of processing to perform
  name: type
  type: string
- description: Determines whether objects are committed in batches or only when complete
  name: commitMode
  type: string
- description: Maximum number of threads to run in parallel
  name: maxParallelism
  type: integer
- description: Number of times to retry on failure
  name: retryCount
  type: integer
- description: Specific tables or partitions to refresh
  name: objects
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-refresh-request-schema.json
slug: power-bi-rest-refresh-request
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: RefreshRequest
---
