---
description: Represents resource utilization statistics for an Oracle Solaris Zone, including CPU, memory, swap, and process metrics collected via the kstat interface and libzonestat library.
layout: schema
name: Oracle Solaris Zone Statistics
properties_list:
- description: Name of the zone
  name: zonename
  type: string
- description: Numeric zone identifier
  name: zone_id
  type: integer
- description: CPU cap value as a percentage of a single CPU (100 = 1 full CPU)
  name: cpu_cap
  type: number
- description: Current CPU usage as a percentage
  name: cpu_usage
  type: number
- description: Number of times zone threads waited due to CPU cap
  name: cpu_nwait
  type: integer
- description: Physical memory cap in bytes
  name: memory_cap
  type: integer
- description: Current physical memory usage (RSS) in bytes
  name: memory_usage
  type: integer
- description: Swap space cap in bytes
  name: swap_cap
  type: integer
- description: Current swap space usage in bytes
  name: swap_usage
  type: integer
- description: Number of processes running in the zone
  name: nprocs
  type: integer
- description: Number of lightweight processes (threads) in the zone
  name: nlwps
  type: integer
- description: Total virtual size of all processes in bytes
  name: pr_size
  type: integer
- description: Total resident set size of all processes in bytes
  name: pr_rss
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-schema.json
slug: solaris-zone-stats
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
title: Oracle Solaris Zone Statistics
---
