---
description: Request body for creating a new virtual server.
layout: schema
name: VirtualServerCreate
properties_list:
- description: Name of the virtual server.
  name: name
  type: string
- description: Administrative partition.
  name: partition
  type: string
- description: Destination address and port in /partition/address:port format.
  name: destination
  type: string
- description: User-defined description.
  name: description
  type: string
- description: IP protocol.
  name: ipProtocol
  type: string
- description: Destination network mask.
  name: mask
  type: string
- description: Default pool full path.
  name: pool
  type: string
- description: Profiles to apply.
  name: profiles
  type: array
- description: Persistence profiles to apply.
  name: persist
  type: array
- description: Source address filter.
  name: source
  type: string
- description: Source port translation behavior.
  name: sourcePort
  type: string
- description: ''
  name: translateAddress
  type: string
- description: ''
  name: translatePort
  type: string
- description: ''
  name: connectionLimit
  type: integer
- description: ''
  name: rules
  type: array
- description: ''
  name: vlans
  type: array
- description: ''
  name: vlansEnabled
  type: boolean
- description: ''
  name: vlansDisabled
  type: boolean
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-virtual-server-create-schema.json
slug: bigip-icontrol-rest-virtual-server-create
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
title: VirtualServerCreate
---
