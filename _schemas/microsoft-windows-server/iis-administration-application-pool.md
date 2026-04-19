---
description: A complete IIS application pool resource with all configuration settings for worker process isolation and management.
layout: schema
name: ApplicationPool
properties_list:
- description: The name of the application pool.
  name: name
  type: string
- description: The unique identifier of the application pool.
  name: id
  type: string
- description: The current status of the application pool.
  name: status
  type: string
- description: Whether the application pool starts automatically when IIS starts.
  name: auto_start
  type: boolean
- description: The managed pipeline mode for the application pool.
  name: pipeline_mode
  type: string
- description: The version of the .NET CLR loaded by the application pool. Empty string for unmanaged code.
  name: managed_runtime_version
  type: string
- description: Whether to enable 32-bit applications on 64-bit Windows.
  name: enable_32bit_win64
  type: boolean
- description: The maximum number of requests that can be queued for the application pool before requests are rejected.
  name: queue_length
  type: integer
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-application-pool-schema.json
slug: iis-administration-application-pool
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ApplicationPool
---
