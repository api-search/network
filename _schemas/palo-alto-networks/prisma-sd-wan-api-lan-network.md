---
description: LANNetwork schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: LANNetwork
properties_list:
- description: Unique identifier for the LAN network.
  name: id
  type: string
- description: Name of the LAN network.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Subnet CIDR for the LAN network (e.g., 192.168.1.0/24).
  name: network
  type: string
- description: VLAN identifier for this LAN network.
  name: vlan_id
  type: integer
- description: Whether the ION device serves DHCP for this network.
  name: dhcp_enabled
  type: boolean
- description: ''
  name: site_id
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-lan-network-schema.json
slug: prisma-sd-wan-api-lan-network
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: LANNetwork
---
