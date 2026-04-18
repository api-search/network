---
description: VlanAttachmentRequest schema from SP Interconnect Manage APIs
layout: schema
name: VlanAttachmentRequest
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: stackType
  type: string
- description: ''
  name: bandwidth
  type: string
- description: ''
  name: bgpPeerAsn
  type: integer
- description: ''
  name: bgpPeerBfdSessionInitMode
  type: string
- description: ''
  name: bgpPeerBfdMinTransmitInterval
  type: integer
- description: ''
  name: bgpPeerBfdMinReceiveInterval
  type: integer
- description: ''
  name: bgpPeerBfdMultiplier
  type: integer
- description: ''
  name: dedicatedConnectionDetails
  type: array
- description: Custom IP address configuration for VLAN attachment BGP peering. Both Cloud Router and Customer Router IP addresses must be provided together with matching prefix lengths (/29 or /30). IP addresses mu
  name: primaryAttachmentCustomIpAddress
  type: object
- description: Custom IP address configuration for VLAN attachment BGP peering. Both Cloud Router and Customer Router IP addresses must be provided together with matching prefix lengths (/29 or /30). IP addresses mu
  name: redundantAttachmentCustomIpAddress
  type: object
- description: ''
  name: bgpPeerMd5AuthEnabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-interconnect-api-vlan-attachment-request-schema.json
slug: sase-multitenant-interconnect-api-vlan-attachment-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: VlanAttachmentRequest
---
