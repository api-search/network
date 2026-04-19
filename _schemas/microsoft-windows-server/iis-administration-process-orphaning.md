---
description: Process orphaning settings that control behavior when a worker process cannot be shut down gracefully.
layout: schema
name: ProcessOrphaning
properties_list:
- description: Whether process orphaning is enabled.
  name: enabled
  type: boolean
- description: The path to an executable to run when a worker process is orphaned.
  name: orphan_action_exe
  type: string
- description: Parameters for the orphan action executable.
  name: orphan_action_params
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-process-orphaning-schema.json
slug: iis-administration-process-orphaning
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ProcessOrphaning
---
