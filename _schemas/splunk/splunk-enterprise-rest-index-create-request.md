---
description: ''
layout: schema
name: IndexCreateRequest
properties_list:
- description: The name for the new index
  name: name
  type: string
- description: Type of data the index will hold
  name: datatype
  type: string
- description: Absolute path for hot and warm bucket storage
  name: homePath
  type: string
- description: Absolute path for cold bucket storage
  name: coldPath
  type: string
- description: Absolute path for thawed bucket storage
  name: thawedPath
  type: string
- description: Maximum total size of the index in MB
  name: maxTotalDataSizeMB
  type: integer
- description: Maximum size of a hot bucket
  name: maxDataSize
  type: string
- description: Seconds until data is frozen
  name: frozenTimePeriodInSecs
  type: integer
- description: Maximum number of hot buckets
  name: maxHotBuckets
  type: integer
- description: Maximum number of warm buckets
  name: maxWarmDBCount
  type: integer
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-index-create-request-schema.json
slug: splunk-enterprise-rest-index-create-request
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
title: IndexCreateRequest
---
