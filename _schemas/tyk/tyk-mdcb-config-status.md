---
description: ''
layout: schema
name: ConfigStatus
properties_list:
- description: ''
  name: listen_port
  type: integer
- description: ''
  name: healthcheck_port
  type: integer
- description: ''
  name: http_port
  type: integer
- description: ''
  name: enable_http_profiler
  type: boolean
- description: ''
  name: server_options
  type: object
- description: ''
  name: http_server_options
  type: object
- description: ''
  name: security
  type: object
- description: ''
  name: storage
  type: object
- description: ''
  name: analytics
  type: object
- description: ''
  name: hash_keys
  type: boolean
- description: ''
  name: session_timeout
  type: integer
- description: ''
  name: forward_analytics_to_pump
  type: boolean
- description: ''
  name: enable_multiple_analytics_keys
  type: boolean
- description: ''
  name: dont_store_selective
  type: boolean
- description: ''
  name: dont_store_aggregate
  type: boolean
- description: ''
  name: org_session_expiration
  type: integer
- description: ''
  name: org_session_cleanup
  type: integer
- description: ''
  name: license
  type: string
- description: ''
  name: aggregates_ignore_tags
  type: string
- description: ''
  name: track_all_paths
  type: boolean
- description: ''
  name: store_analytics_per_minute
  type: boolean
- description: ''
  name: ignore_tag_prefix_list
  type: string
- description: ''
  name: threshold_len_tag_list
  type: integer
- description: ''
  name: omit_analytics_index_creation
  type: boolean
- description: ''
  name: enable_separate_analytics_store
  type: boolean
- description: ''
  name: analytics_storage
  type: object
- description: ''
  name: log_level
  type: string
- description: ''
  name: enable_key_logging
  type: boolean
- description: ''
  name: sync_worker_config
  type: object
- description: ''
  name: enable_ownership
  type: boolean
provider_name: Tyk
provider_slug: tyk
schema_file: json-schema/tyk-mdcb-config-status-schema.json
slug: tyk-mdcb-config-status
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
title: ConfigStatus
---
