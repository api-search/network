---
description: Physical memory cap statistics
layout: schema
name: MemoryCapStats
properties_list:
- description: Physical memory cap in bytes
  name: physcap
  type: integer
- description: Current resident set size in bytes
  name: rss
  type: integer
- description: Number of times memory went over the cap
  name: nover
  type: integer
- description: Total bytes paged out due to capping
  name: pagedout
  type: integer
- description: Pages paged in
  name: pgpgin
  type: integer
- description: Anonymous pages paged in
  name: anonpgin
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-stats-memory-cap-stats-schema.json
slug: solaris-zone-stats-memory-cap-stats
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
title: MemoryCapStats
---
