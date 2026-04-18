---
description: ''
layout: schema
name: SystemMemoryStats
properties_list:
- description: Total physical memory pages
  name: physmem
  type: integer
- description: Free memory pages
  name: freemem
  type: integer
- description: Available real memory pages
  name: availrmem
  type: integer
- description: Lotsfree threshold
  name: lotsfree
  type: integer
- description: Desfree threshold
  name: desfree
  type: integer
- description: Minfree threshold
  name: minfree
  type: integer
- description: Pages used by kernel
  name: pp_kernel
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-system-memory-stats-schema.json
slug: solaris-zone-stats-system-memory-stats
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
title: SystemMemoryStats
---
