---
description: ''
layout: schema
name: EventSearchResult
properties_list:
- description: ''
  name: events
  type: array
- description: Minimum event ID in results
  name: min_id
  type: string
- description: Maximum event ID in results
  name: max_id
  type: string
- description: Whether results include the earliest matching event
  name: reached_beginning
  type: boolean
- description: ''
  name: min_time_at
  type: string
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-papertrail-event-search-result-schema.json
slug: solarwinds-papertrail-event-search-result
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
title: EventSearchResult
---
