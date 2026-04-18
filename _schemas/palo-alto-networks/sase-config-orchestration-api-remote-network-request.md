---
description: RemoteNetworkRequest schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: RemoteNetworkRequest
properties_list:
- description: Display name for the remote network.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: Prisma Access gateway location name.
  name: location
  type: string
- description: Network subnets at the remote site in CIDR notation.
  name: subnets
  type: array
- description: ''
  name: ike_gateway
  type: object
- description: Requested bandwidth allocation in Mbps.
  name: bandwidth_mbps
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-remote-network-request-schema.json
slug: sase-config-orchestration-api-remote-network-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RemoteNetworkRequest
---
