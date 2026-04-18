---
description: ''
layout: schema
name: VmCpuStats
properties_list:
- description: Nanoseconds spent idle
  name: cpu_nsec_idle
  type: integer
- description: Nanoseconds spent in kernel mode
  name: cpu_nsec_kernel
  type: integer
- description: Nanoseconds spent in user mode
  name: cpu_nsec_user
  type: integer
- description: Nanoseconds spent in DTrace
  name: cpu_nsec_dtrace
  type: integer
- description: Nanoseconds spent handling interrupts
  name: cpu_nsec_intr
  type: integer
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-monitoring-vm-cpu-stats-schema.json
slug: solaris-zone-monitoring-vm-cpu-stats
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
title: VmCpuStats
---
