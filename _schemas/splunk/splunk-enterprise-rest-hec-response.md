---
description: ''
layout: schema
name: HecResponse
properties_list:
- description: Human-readable status message
  name: text
  type: string
- description: Numeric status code
  name: code
  type: integer
- description: For batched events, the index of the first invalid event
  name: invalid-event-number
  type: integer
- description: Acknowledgment ID for tracking indexing status (when indexer acknowledgment is enabled)
  name: ackId
  type: integer
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-hec-response-schema.json
slug: splunk-enterprise-rest-hec-response
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
title: HecResponse
---
