---
description: ''
layout: schema
name: CpuInfo
properties_list:
- description: CPU brand string
  name: brand
  type: string
- description: Physical chip ID
  name: chip_id
  type: integer
- description: CPU clock speed in MHz
  name: clock_MHz
  type: integer
- description: Core ID within the chip
  name: core_id
  type: integer
- description: CPU type identifier
  name: cpu_type
  type: string
- description: CPU implementation description
  name: implementation
  type: string
- description: Number of cores per chip
  name: ncore_per_chip
  type: integer
- description: CPU state (on-line, off-line)
  name: state
  type: string
- description: CPU vendor identifier
  name: vendor_id
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-monitoring-cpu-info-schema.json
slug: solaris-zone-monitoring-cpu-info
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
title: CpuInfo
---
