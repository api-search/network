---
description: ''
layout: schema
name: LogEvent
properties_list:
- description: Unique event identifier
  name: id
  type: string
- description: Event timestamp in milliseconds
  name: timestamp
  type: integer
- description: Raw log message
  name: logmsg
  type: string
- description: Detected log types
  name: logtypes
  type: array
- description: Parsed event fields
  name: event
  type: object
- description: Tags associated with the event
  name: tags
  type: array
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-loggly-log-event-schema.json
slug: solarwinds-loggly-log-event
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
title: LogEvent
---
