---
description: ''
layout: schema
name: Incident
properties_list:
- description: Unique incident identifier
  name: id
  type: integer
- description: Human-readable incident number
  name: number
  type: integer
- description: Incident title
  name: name
  type: string
- description: Incident description
  name: description
  type: string
- description: Current state
  name: state
  type: string
- description: Priority level
  name: priority
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-service-desk-incident-schema.json
slug: solarwinds-service-desk-incident
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
title: Incident
---
