---
description: IKEGateway schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: IKEGateway
properties_list:
- description: Public IP address of the remote peer gateway.
  name: peer_ip
  type: string
- description: IKE peer identity.
  name: peer_id
  type: string
- description: Prisma Access local IKE gateway IP address.
  name: local_ip
  type: string
- description: IKE protocol version.
  name: ike_version
  type: string
- description: IKE authentication method.
  name: authentication_type
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-ike-gateway-schema.json
slug: sase-config-orchestration-api-ike-gateway
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
