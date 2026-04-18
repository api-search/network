---
description: ''
layout: schema
name: Result
properties_list:
- description: Probe server ID
  name: probeid
  type: integer
- description: Test timestamp (Unix)
  name: time
  type: integer
- description: Result status
  name: status
  type: string
- description: Response time in milliseconds
  name: responsetime
  type: integer
- description: Status description
  name: statusdesc
  type: string
- description: Detailed status description
  name: statusdesclong
  type: string
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-pingdom-result-schema.json
slug: solarwinds-pingdom-result
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
title: Result
---
