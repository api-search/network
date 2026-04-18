---
description: PathRule schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: PathRule
properties_list:
- description: Unique identifier for the path rule.
  name: id
  type: string
- description: Name of the path rule.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Application identifiers this path rule applies to.
  name: app_filters
  type: array
- description: Ordered list of preferred WAN paths for traffic steering.
  name: preferred_paths
  type: array
- description: SLA thresholds that trigger path switching.
  name: sla_threshold
  type: object
- description: Whether the rule is active.
  name: enabled
  type: boolean
- description: Rule evaluation priority. Lower numbers are evaluated first.
  name: priority
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-path-rule-schema.json
slug: prisma-sd-wan-api-path-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: PathRule
---
