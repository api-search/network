---
description: ''
layout: schema
name: HecTokenCreateRequest
properties_list:
- description: Name for the new HEC token
  name: name
  type: string
- description: Default destination index
  name: index
  type: string
- description: Comma-separated list of allowed indexes
  name: indexes
  type: string
- description: Default sourcetype
  name: sourcetype
  type: string
- description: Default source value
  name: source
  type: string
- description: Default host value
  name: host
  type: string
- description: Whether to create the token in disabled state
  name: disabled
  type: boolean
- description: Whether to enable indexer acknowledgment
  name: useACK
  type: boolean
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-hec-token-create-request-schema.json
slug: splunk-enterprise-rest-hec-token-create-request
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
title: HecTokenCreateRequest
---
