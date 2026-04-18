---
description: IKEGatewayConfig schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: IKEGatewayConfig
properties_list:
- description: Public IP address of the remote peer gateway.
  name: peer_ip
  type: string
- description: IKE peer identity. Defaults to the peer IP if omitted.
  name: peer_id
  type: string
- description: ''
  name: ike_version
  type: string
- description: ''
  name: authentication_type
  type: string
- description: Pre-shared key for IKE authentication.
  name: pre_shared_key
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-ike-gateway-config-schema.json
slug: sase-config-orchestration-api-ike-gateway-config
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IKEGatewayConfig
---
