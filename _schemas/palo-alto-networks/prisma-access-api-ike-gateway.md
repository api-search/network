---
description: IKEGateway schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: IKEGateway
properties_list:
- description: Unique identifier for the IKE gateway.
  name: id
  type: string
- description: Name of the IKE gateway.
  name: name
  type: string
- description: IKE protocol version.
  name: version
  type: string
- description: Peer IP address configuration.
  name: peer_address
  type: object
- description: IKE authentication configuration.
  name: authentication
  type: object
- description: ''
  name: local_id
  type: object
- description: ''
  name: peer_id
  type: object
- description: ''
  name: folder
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-ike-gateway-schema.json
slug: prisma-access-api-ike-gateway
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IKEGateway
---
