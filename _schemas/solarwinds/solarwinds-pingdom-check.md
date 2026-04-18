---
description: ''
layout: schema
name: Check
properties_list:
- description: Unique check identifier
  name: id
  type: integer
- description: Check name
  name: name
  type: string
- description: Check type
  name: type
  type: string
- description: Target hostname
  name: hostname
  type: string
- description: Current check status
  name: status
  type: string
- description: Check interval in minutes
  name: resolution
  type: integer
- description: Last response time in milliseconds
  name: lastresponsetime
  type: integer
- description: Last test timestamp (Unix)
  name: lasttesttime
  type: integer
- description: Creation timestamp (Unix)
  name: created
  type: integer
- description: ''
  name: tags
  type: array
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-pingdom-check-schema.json
slug: solarwinds-pingdom-check
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
title: Check
---
