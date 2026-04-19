---
description: ''
layout: schema
name: SearchJobCreateRequest
properties_list:
- description: The SPL search query to execute
  name: search
  type: string
- description: Earliest time for the search using relative or absolute time format
  name: earliest_time
  type: string
- description: Latest time for the search
  name: latest_time
  type: string
- description: The search mode
  name: search_mode
  type: string
- description: Execution mode. Normal runs asynchronously, oneshot runs synchronously, blocking waits for completion.
  name: exec_mode
  type: string
- description: Maximum number of results to return
  name: max_count
  type: integer
- description: Maximum time in seconds before the search is finalized
  name: max_time
  type: integer
- description: Number of seconds to keep the search after processing has stopped
  name: timeout
  type: integer
- description: Comma-separated list of required fields to include in results
  name: rf
  type: string
- description: Application namespace for the search
  name: namespace
  type: string
- description: Optional custom search ID. If not specified, Splunk generates one automatically.
  name: id
  type: string
- description: Number of status buckets to generate for the search timeline. Set to a value greater than 0 to enable timeline.
  name: status_buckets
  type: integer
- description: Seconds of inactivity after which the search is automatically cancelled. 0 means never auto-cancel.
  name: auto_cancel
  type: integer
- description: Auto-finalize the search after this number of events have been processed. 0 disables auto-finalize.
  name: auto_finalize_ec
  type: integer
- description: Seconds of inactivity after which the search is automatically paused. 0 means never auto-pause.
  name: auto_pause
  type: integer
- description: Whether to enable lookups during the search
  name: enable_lookups
  type: boolean
- description: Whether to reload macro definitions before the search
  name: reload_macros
  type: boolean
- description: How frequently to invoke the reduce phase (seconds)
  name: reduce_freq
  type: integer
- description: Whether to run the search in a separate process
  name: spawn_process
  type: boolean
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-search-job-create-request-schema.json
slug: splunk-enterprise-rest-search-job-create-request
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
title: SearchJobCreateRequest
---
