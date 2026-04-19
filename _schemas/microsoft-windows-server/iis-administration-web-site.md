---
description: A complete IIS web site resource including configuration, bindings, application pool assignment, and HAL links to related resources.
layout: schema
name: WebSite
properties_list:
- description: The name of the web site.
  name: name
  type: string
- description: The unique identifier of the web site.
  name: id
  type: string
- description: The physical file system path for the web site root.
  name: physical_path
  type: string
- description: The IIS site key identifier.
  name: key
  type: string
- description: The current status of the web site.
  name: status
  type: string
- description: Whether the web site starts automatically when IIS starts.
  name: server_auto_start
  type: boolean
- description: The protocols enabled for this web site, as a comma-separated list.
  name: enabled_protocols
  type: string
- description: The list of bindings configured for this web site.
  name: bindings
  type: array
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-web-site-schema.json
slug: iis-administration-web-site
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: WebSite
---
