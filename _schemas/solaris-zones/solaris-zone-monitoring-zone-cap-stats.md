---
description: ''
layout: schema
name: ZoneCapStats
properties_list:
- description: Zone name
  name: zonename
  type: string
- description: Numeric zone ID
  name: zone_id
  type: integer
- description: CPU cap value
  name: cpu_cap
  type: number
- description: Current CPU usage
  name: cpu_usage
  type: number
- description: Memory cap in bytes
  name: memory_cap
  type: integer
- description: Current memory usage in bytes
  name: memory_usage
  type: integer
- description: Swap cap in bytes
  name: swap_cap
  type: integer
- description: Current swap usage in bytes
  name: swap_usage
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-monitoring-zone-cap-stats-schema.json
slug: solaris-zone-monitoring-zone-cap-stats
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
title: ZoneCapStats
---
