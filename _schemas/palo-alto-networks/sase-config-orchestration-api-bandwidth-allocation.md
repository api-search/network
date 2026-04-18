---
description: BandwidthAllocation schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: BandwidthAllocation
properties_list:
- description: Prisma Access location name.
  name: location
  type: string
- description: Geographic region.
  name: region
  type: string
- description: Total licensed bandwidth at this location in Mbps.
  name: licensed_bandwidth_mbps
  type: integer
- description: Bandwidth currently allocated to remote networks in Mbps.
  name: allocated_bandwidth_mbps
  type: integer
- description: Remaining available bandwidth in Mbps.
  name: available_bandwidth_mbps
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-bandwidth-allocation-schema.json
slug: sase-config-orchestration-api-bandwidth-allocation
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BandwidthAllocation
---
