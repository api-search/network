---
description: ServiceConnection schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: ServiceConnection
properties_list:
- description: Unique identifier for the service connection.
  name: id
  type: string
- description: Name of the service connection.
  name: name
  type: string
- description: Prisma Access compute region.
  name: region
  type: string
- description: Name of the associated IPSec tunnel.
  name: ipsec_tunnel
  type: string
- description: Internal subnets accessible through this connection.
  name: subnets
  type: array
- description: NAT pool CIDR for source translation.
  name: nat_pool
  type: string
- description: Whether QoS is enabled on this connection.
  name: qos_enabled
  type: boolean
- description: ''
  name: folder
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-service-connection-schema.json
slug: prisma-access-api-service-connection
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ServiceConnection
---
