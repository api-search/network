---
description: An asset tracked in the XSIAM asset inventory.
layout: schema
name: Asset
properties_list:
- description: ''
  name: asset_id
  type: string
- description: ''
  name: asset_name
  type: string
- description: ''
  name: asset_type
  type: string
- description: ''
  name: operating_system
  type: string
- description: ''
  name: ip_addresses
  type: array
- description: Asset risk score (0.0 to 100.0).
  name: risk_score
  type: number
- description: First observation timestamp as Unix epoch milliseconds.
  name: first_seen
  type: integer
- description: ''
  name: last_seen
  type: integer
- description: ''
  name: tags
  type: array
- description: Data sources that reported this asset.
  name: sources
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-asset-schema.json
slug: cortex-xsiam-api-asset
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Asset
---
