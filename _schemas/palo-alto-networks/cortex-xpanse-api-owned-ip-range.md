---
description: An IP range owned by the organization and monitored by Xpanse.
layout: schema
name: OwnedIpRange
properties_list:
- description: ''
  name: range_id
  type: string
- description: IP range in CIDR notation (e.g., 203.0.113.0/24).
  name: cidr
  type: string
- description: ''
  name: first_ip
  type: string
- description: ''
  name: last_ip
  type: string
- description: Number of IP addresses in the range.
  name: range_size
  type: integer
- description: ''
  name: business_units
  type: array
- description: ''
  name: attribution_reason
  type: string
- description: Range creation timestamp as Unix epoch milliseconds.
  name: created
  type: integer
- description: ''
  name: modified
  type: integer
- description: ''
  name: tags
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xpanse-api-owned-ip-range-schema.json
slug: cortex-xpanse-api-owned-ip-range
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: OwnedIpRange
---
