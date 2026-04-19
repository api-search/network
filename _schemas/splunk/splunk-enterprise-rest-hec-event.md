---
description: ''
layout: schema
name: HecEvent
properties_list:
- description: Event timestamp in epoch time (seconds since 1970-01-01). If omitted, Splunk uses the current time.
  name: time
  type: string
- description: Hostname or IP address of the event source
  name: host
  type: string
- description: Source of the event
  name: source
  type: string
- description: Source type for the event
  name: sourcetype
  type: string
- description: Destination index for the event
  name: index
  type: string
- description: The event data. Can be a string or a JSON object. This is the actual data payload to be indexed.
  name: event
  type: string
- description: Additional metadata fields to associate with the event. These fields are indexed as metadata and can be searched.
  name: fields
  type: object
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-hec-event-schema.json
slug: splunk-enterprise-rest-hec-event
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
title: HecEvent
---
