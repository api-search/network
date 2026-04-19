---
description: ''
layout: schema
name: MonitorInputCreateRequest
properties_list:
- description: The file or directory path to monitor
  name: name
  type: string
- description: Destination index
  name: index
  type: string
- description: Source type to assign
  name: sourcetype
  type: string
- description: Source value to assign
  name: source
  type: string
- description: Host value to assign
  name: host
  type: string
- description: Whether to create the input in disabled state
  name: disabled
  type: boolean
- description: Start monitoring from end of file
  name: followTail
  type: boolean
- description: Recursively monitor subdirectories
  name: recursive
  type: boolean
- description: Regex pattern for files to include
  name: whitelist
  type: string
- description: Regex pattern for files to exclude
  name: blacklist
  type: string
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-monitor-input-create-request-schema.json
slug: splunk-enterprise-rest-monitor-input-create-request
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
title: MonitorInputCreateRequest
---
