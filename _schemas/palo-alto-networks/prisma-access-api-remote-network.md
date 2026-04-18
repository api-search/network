---
description: RemoteNetwork schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: RemoteNetwork
properties_list:
- description: Unique identifier for the remote network.
  name: id
  type: string
- description: Name of the remote network.
  name: name
  type: string
- description: Prisma Access compute region (e.g., us-east-1, eu-west-1).
  name: region
  type: string
- description: License type assigned to this remote network.
  name: license_type
  type: string
- description: Service provider node name for the Prisma Access gateway location.
  name: spn_name
  type: string
- description: Enable or disable ECMP load balancing.
  name: ecmp_load_balancing
  type: string
- description: Local subnets at the remote network site.
  name: subnets
  type: array
- description: Folder containing this remote network.
  name: folder
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-remote-network-schema.json
slug: prisma-access-api-remote-network
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
