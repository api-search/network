---
description: Swap cap statistics
layout: schema
name: SwapCapStats
properties_list:
- description: Swap cap in bytes
  name: swapcap
  type: integer
- description: Current swap usage in bytes
  name: usage
  type: integer
- description: Number of times swap exceeded the cap
  name: nover
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-swap-cap-stats-schema.json
slug: solaris-zone-stats-swap-cap-stats
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
title: SwapCapStats
---
