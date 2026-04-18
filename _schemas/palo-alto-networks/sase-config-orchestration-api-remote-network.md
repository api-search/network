---
description: RemoteNetwork schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: RemoteNetwork
properties_list:
- description: Unique identifier of the remote network.
  name: id
  type: string
- description: Display name of the remote network.
  name: name
  type: string
- description: Description of the remote network's location or purpose.
  name: description
  type: string
- description: Prisma Access gateway location for this tunnel.
  name: location
  type: string
- description: Network subnets at the remote site (CIDR notation).
  name: subnets
  type: array
- description: ''
  name: ike_gateway
  type: object
- description: ''
  name: ipsec_tunnel
  type: object
- description: Current IPsec tunnel connection status.
  name: tunnel_status
  type: string
- description: Allocated bandwidth in Mbps for this remote network.
  name: bandwidth_mbps
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-remote-network-schema.json
slug: sase-config-orchestration-api-remote-network
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RemoteNetwork
---
