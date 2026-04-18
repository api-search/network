---
description: Summary of an internet-exposed asset discovered by Xpanse.
layout: schema
name: AssetInternetExposure
properties_list:
- description: List of ASM identifiers for this asset.
  name: asm_id_list
  type: array
- description: Asset hostname, IP address, or identifier.
  name: asset_name
  type: string
- description: ''
  name: asset_type
  type: string
- description: IP addresses associated with this asset.
  name: ip_address
  type: array
- description: Domain names associated with this asset.
  name: domain
  type: array
- description: ''
  name: ipv6_address
  type: array
- description: Cloud provider resource identifier.
  name: cloud_id
  type: string
- description: ''
  name: cloud_provider
  type: string
- description: ''
  name: externally_detected_providers
  type: array
- description: Business units associated with this asset.
  name: business_units
  type: array
- description: ''
  name: tags
  type: array
- description: Asset first discovery timestamp as Unix epoch milliseconds.
  name: created
  type: integer
- description: Most recent observation timestamp as Unix epoch milliseconds.
  name: last_observed
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xpanse-api-asset-internet-exposure-schema.json
slug: cortex-xpanse-api-asset-internet-exposure
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AssetInternetExposure
---
