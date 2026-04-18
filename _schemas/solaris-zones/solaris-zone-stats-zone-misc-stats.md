---
description: Zone miscellaneous statistics
layout: schema
name: ZoneMiscStats
properties_list:
- description: ''
  name: zonename
  type: string
- description: ''
  name: zone_id
  type: integer
- description: Number of processes in the zone
  name: nprocs
  type: integer
- description: Number of lightweight processes in the zone
  name: nlwps
  type: integer
- description: Total process size in bytes
  name: pr_size
  type: integer
- description: Total resident set size in bytes
  name: pr_rss
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-zone-misc-stats-schema.json
slug: solaris-zone-stats-zone-misc-stats
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
title: ZoneMiscStats
---
