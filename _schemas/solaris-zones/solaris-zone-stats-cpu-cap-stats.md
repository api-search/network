---
description: CPU cap statistics
layout: schema
name: CpuCapStats
properties_list:
- description: CPU cap value in microseconds per second
  name: value
  type: integer
- description: Current CPU usage in microseconds per second
  name: usage
  type: integer
- description: Number of times threads waited due to cap
  name: nwait
  type: integer
- description: Time spent below the cap in nanoseconds
  name: below
  type: integer
- description: Time spent above the cap in nanoseconds
  name: above
  type: integer
- description: Maximum CPU usage observed
  name: maxusage
  type: integer
- description: Zone name
  name: zonename
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-cpu-cap-stats-schema.json
slug: solaris-zone-stats-cpu-cap-stats
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
title: CpuCapStats
---
