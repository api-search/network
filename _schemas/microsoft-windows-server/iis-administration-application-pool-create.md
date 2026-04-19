---
description: Request body for creating a new application pool.
layout: schema
name: ApplicationPoolCreate
properties_list:
- description: The name of the application pool to create.
  name: name
  type: string
- description: ''
  name: auto_start
  type: boolean
- description: ''
  name: pipeline_mode
  type: string
- description: ''
  name: managed_runtime_version
  type: string
- description: ''
  name: enable_32bit_win64
  type: boolean
- description: ''
  name: queue_length
  type: integer
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-application-pool-create-schema.json
slug: iis-administration-application-pool-create
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ApplicationPoolCreate
---
