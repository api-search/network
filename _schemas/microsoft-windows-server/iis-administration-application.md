---
description: A complete IIS web application resource. Applications belong to a single web site and handle requests at a specific virtual path.
layout: schema
name: Application
properties_list:
- description: The full location path combining the web site name and application path.
  name: location
  type: string
- description: The virtual path of the application relative to the web site root.
  name: path
  type: string
- description: The unique identifier of the application.
  name: id
  type: string
- description: The physical file system path for the application.
  name: physical_path
  type: string
- description: The protocols enabled for this application, as a comma-separated list.
  name: enabled_protocols
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-application-schema.json
slug: iis-administration-application
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: Application
---
