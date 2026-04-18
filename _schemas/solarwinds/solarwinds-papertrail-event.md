---
description: ''
layout: schema
name: Event
properties_list:
- description: Unique event identifier
  name: id
  type: string
- description: When the event was received
  name: received_at
  type: string
- description: When the event was generated
  name: generated_at
  type: string
- description: Human-readable received timestamp
  name: display_received_at
  type: string
- description: Source IP address
  name: source_ip
  type: string
- description: Source system name
  name: source_name
  type: string
- description: Source system ID
  name: source_id
  type: integer
- description: Hostname
  name: hostname
  type: string
- description: Program name
  name: program
  type: string
- description: Syslog severity
  name: severity
  type: string
- description: Syslog facility
  name: facility
  type: string
- description: Log message content
  name: message
  type: string
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-papertrail-event-schema.json
slug: solarwinds-papertrail-event
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
title: Event
---
