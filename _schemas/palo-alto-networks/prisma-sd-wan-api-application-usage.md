---
description: ApplicationUsage schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: ApplicationUsage
properties_list:
- description: Application name.
  name: application
  type: string
- description: Site where the application traffic was observed.
  name: site_id
  type: string
- description: Uploaded bytes for the application.
  name: bytes_up
  type: integer
- description: Downloaded bytes for the application.
  name: bytes_down
  type: integer
- description: Number of application sessions.
  name: sessions
  type: integer
- description: Average latency for application traffic.
  name: avg_latency_ms
  type: number
- description: Time bucket for the usage data.
  name: timestamp
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-application-usage-schema.json
slug: prisma-sd-wan-api-application-usage
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ApplicationUsage
---
