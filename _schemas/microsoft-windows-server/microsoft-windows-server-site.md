---
description: Schema for an IIS web site resource as exposed by the Microsoft IIS Administration API. Web sites are a core entity of IIS that determine where and how HTTP requests will be handled, including binding configuration, application pool assignment, and resource limits.
layout: schema
name: IIS Web Site
properties_list:
- description: The display name of the web site.
  name: name
  type: string
- description: The unique identifier assigned to the web site by the IIS Administration API.
  name: id
  type: string
- description: The physical file system path for the web site root directory. Environment variables such as %SystemDrive% are supported.
  name: physical_path
  type: string
- description: The IIS site key identifier, corresponding to the site ID in IIS configuration.
  name: key
  type: string
- description: The current operational status of the web site.
  name: status
  type: string
- description: Whether the web site starts automatically when the IIS service starts.
  name: server_auto_start
  type: boolean
- description: A comma-separated list of protocols enabled for this web site.
  name: enabled_protocols
  type: string
- description: Resource limits governing connection behavior and URL processing for the web site.
  name: limits
  type: object
- description: The bindings that define the protocols, IP addresses, ports, and hostnames the web site listens on. At minimum, a binding must specify a protocol, IP address, and port.
  name: bindings
  type: array
- description: The application pool assigned to handle requests for this web site.
  name: application_pool
  type: object
- description: HAL-style hypermedia links to related resources.
  name: _links
  type: object
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/microsoft-windows-server-site-schema.json
slug: microsoft-windows-server-site
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: IIS Web Site
---
