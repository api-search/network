---
description: Request body for updating a web site. Only include properties that should be changed. Note that list properties like bindings replace the entire list.
layout: schema
name: WebSiteUpdate
properties_list:
- description: The name of the web site.
  name: name
  type: string
- description: The physical file system path for the web site root.
  name: physical_path
  type: string
- description: The full list of desired bindings. Existing bindings not included in this list will be removed.
  name: bindings
  type: array
- description: ''
  name: application_pool
  type: object
- description: ''
  name: server_auto_start
  type: boolean
- description: ''
  name: enabled_protocols
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-web-site-update-schema.json
slug: iis-administration-web-site-update
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: WebSiteUpdate
---
