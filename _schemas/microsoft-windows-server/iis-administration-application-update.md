---
description: Request body for updating a web application. Only include properties that should be changed.
layout: schema
name: ApplicationUpdate
properties_list:
- description: The virtual path for the application.
  name: path
  type: string
- description: The physical file system path for the application.
  name: physical_path
  type: string
- description: ''
  name: application_pool
  type: object
- description: ''
  name: enabled_protocols
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-application-update-schema.json
slug: iis-administration-application-update
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ApplicationUpdate
---
