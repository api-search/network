---
description: ''
layout: schema
name: CheckCreate
properties_list:
- description: Check name
  name: name
  type: string
- description: Target hostname or IP
  name: host
  type: string
- description: Check type
  name: type
  type: string
- description: Check interval in minutes
  name: resolution
  type: integer
- description: Whether the check is paused
  name: paused
  type: boolean
- description: Use SSL/TLS
  name: encryption
  type: boolean
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-pingdom-check-create-schema.json
slug: solarwinds-pingdom-check-create
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
title: CheckCreate
---
