---
description: Request body for creating a new web site.
layout: schema
name: WebSiteCreate
properties_list:
- description: The name of the web site to create.
  name: name
  type: string
- description: The physical file system path for the web site root directory. The directory must exist.
  name: physical_path
  type: string
- description: The bindings for the web site.
  name: bindings
  type: array
- description: Optional application pool assignment.
  name: application_pool
  type: object
- description: Whether the web site starts automatically when IIS starts.
  name: server_auto_start
  type: boolean
- description: The protocols enabled for this web site.
  name: enabled_protocols
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-web-site-create-schema.json
slug: iis-administration-web-site-create
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: WebSiteCreate
---
