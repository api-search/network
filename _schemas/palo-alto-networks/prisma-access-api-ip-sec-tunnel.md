---
description: IPSecTunnel schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: IPSecTunnel
properties_list:
- description: Unique identifier for the IPSec tunnel.
  name: id
  type: string
- description: Name of the IPSec tunnel.
  name: name
  type: string
- description: Auto-key IKE configuration for the tunnel.
  name: auto_key
  type: object
- description: ''
  name: tunnel_monitor
  type: object
- description: Whether anti-replay protection is enabled.
  name: anti_replay
  type: boolean
- description: ''
  name: folder
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-ip-sec-tunnel-schema.json
slug: prisma-access-api-ip-sec-tunnel
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IPSecTunnel
---
