---
description: A gateway device managed by Aruba Central providing routing, VPN, and SD-WAN functionality.
layout: schema
name: Gateway
properties_list:
- description: Serial number of the gateway.
  name: serial
  type: string
- description: Name of the gateway.
  name: name
  type: string
- description: MAC address of the gateway.
  name: macaddr
  type: string
- description: Hardware model.
  name: model
  type: string
- description: Operational status.
  name: status
  type: string
- description: IP address of the gateway.
  name: ip_address
  type: string
- description: Firmware version.
  name: firmware_version
  type: string
- description: Configuration group.
  name: group_name
  type: string
- description: Site assignment.
  name: site
  type: string
- description: Uptime in seconds.
  name: uptime
  type: integer
- description: Number of connected clients.
  name: client_count
  type: integer
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-gateway-schema.json
slug: aruba-central-gateway
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Gateway
---
