---
description: ''
layout: schema
name: System
properties_list:
- description: System ID
  name: id
  type: integer
- description: System name
  name: name
  type: string
- description: ''
  name: last_event_at
  type: string
- description: ''
  name: auto_delete
  type: boolean
- description: ''
  name: ip_address
  type: string
- description: ''
  name: hostname
  type: string
- description: ''
  name: syslog
  type: object
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-papertrail-system-schema.json
slug: solarwinds-papertrail-system
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
title: System
---
