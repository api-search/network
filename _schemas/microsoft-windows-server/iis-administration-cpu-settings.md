---
description: CPU usage settings for the application pool.
layout: schema
name: CpuSettings
properties_list:
- description: The maximum CPU usage percentage (in 1/1000ths of a percent) allowed for the application pool.
  name: limit
  type: integer
- description: The interval in minutes for CPU limit monitoring.
  name: limit_interval
  type: integer
- description: The action to take when the CPU limit is exceeded.
  name: action
  type: string
- description: Whether processor affinity is enabled.
  name: processor_affinity_enabled
  type: boolean
- description: The 32-bit processor affinity mask.
  name: processor_affinity_mask32
  type: string
- description: The 64-bit processor affinity mask.
  name: processor_affinity_mask64
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-cpu-settings-schema.json
slug: iis-administration-cpu-settings
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: CpuSettings
---
