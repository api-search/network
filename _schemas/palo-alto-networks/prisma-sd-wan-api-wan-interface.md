---
description: WANInterface schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: WANInterface
properties_list:
- description: Unique identifier for the WAN interface.
  name: id
  type: string
- description: Name of the WAN interface.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Type of WAN connection.
  name: type
  type: string
- description: Downstream bandwidth in Mbps.
  name: link_bw_down
  type: number
- description: Upstream bandwidth in Mbps.
  name: link_bw_up
  type: number
- description: Cost metric for path selection. Lower cost is preferred.
  name: cost
  type: integer
- description: Whether Link Quality Monitoring is enabled.
  name: lqm_enabled
  type: boolean
- description: WAN interface label for policy-based routing.
  name: label_id
  type: string
- description: ''
  name: site_id
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-wan-interface-schema.json
slug: prisma-sd-wan-api-wan-interface
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: WANInterface
---
