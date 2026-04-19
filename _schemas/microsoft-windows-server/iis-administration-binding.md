---
description: Defines the protocol, IP address, port, and optional hostname that a web site listens on. The binding_information property format is '{ip_address}:{port}:{hostname}' for HTTP and HTTPS protocols.
layout: schema
name: Binding
properties_list:
- description: The protocol for this binding (e.g., http, https, net.tcp).
  name: protocol
  type: string
- description: Combined binding string in the format '{ip_address}:{port}:{hostname}'.
  name: binding_information
  type: string
- description: The IP address to bind to. Use '*' for all addresses.
  name: ip_address
  type: string
- description: The port number to listen on.
  name: port
  type: integer
- description: The hostname for host header-based routing.
  name: hostname
  type: string
- description: Whether Server Name Indication (SNI) is required for this binding.
  name: require_sni
  type: boolean
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-binding-schema.json
slug: iis-administration-binding
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: Binding
---
