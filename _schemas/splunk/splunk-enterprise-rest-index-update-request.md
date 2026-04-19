---
description: ''
layout: schema
name: IndexUpdateRequest
properties_list:
- description: Maximum total size of the index in MB
  name: maxTotalDataSizeMB
  type: integer
- description: Seconds until data is frozen
  name: frozenTimePeriodInSecs
  type: integer
- description: Maximum number of hot buckets
  name: maxHotBuckets
  type: integer
- description: Maximum number of warm buckets
  name: maxWarmDBCount
  type: integer
- description: Whether to disable the index
  name: disabled
  type: boolean
- description: Path to archive frozen buckets to. If not set, frozen data is deleted.
  name: coldToFrozenDir
  type: string
- description: Script to run when freezing buckets
  name: coldToFrozenScript
  type: string
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-index-update-request-schema.json
slug: splunk-enterprise-rest-index-update-request
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
title: IndexUpdateRequest
---
