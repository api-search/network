---
description: Alarm schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: Alarm
properties_list:
- description: Unique alarm identifier.
  name: id
  type: string
- description: Alarm type identifier.
  name: type
  type: string
- description: Alarm severity level.
  name: severity
  type: string
- description: Site where the alarm was generated.
  name: site_id
  type: string
- description: Name of the site where the alarm was generated.
  name: site_name
  type: string
- description: ION element identifier that generated the alarm.
  name: element_id
  type: string
- description: Human-readable alarm description.
  name: message
  type: string
- description: Whether the alarm has been acknowledged.
  name: acknowledged
  type: boolean
- description: User who acknowledged the alarm.
  name: acknowledged_by
  type: string
- description: Timestamp when the alarm was acknowledged.
  name: acknowledged_at
  type: string
- description: Timestamp when the alarm was raised.
  name: raised_at
  type: string
- description: Timestamp when the alarm was cleared. Null if still active.
  name: cleared_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-alarm-schema.json
slug: prisma-sd-wan-api-alarm
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Alarm
---
