---
description: Request body for creating a new web application.
layout: schema
name: ApplicationCreate
properties_list:
- description: The virtual path for the application relative to the web site root.
  name: path
  type: string
- description: The physical file system path for the application. The directory must exist.
  name: physical_path
  type: string
- description: The web site that the application should belong to.
  name: website
  type: object
- description: Optional application pool assignment.
  name: application_pool
  type: object
- description: The protocols enabled for this application.
  name: enabled_protocols
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-application-create-schema.json
slug: iis-administration-application-create
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: ApplicationCreate
---
