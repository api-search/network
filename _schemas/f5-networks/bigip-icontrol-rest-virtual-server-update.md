---
description: Request body for updating a virtual server.
layout: schema
name: VirtualServerUpdate
properties_list:
- description: ''
  name: description
  type: string
- description: ''
  name: destination
  type: string
- description: ''
  name: ipProtocol
  type: string
- description: ''
  name: mask
  type: string
- description: ''
  name: pool
  type: string
- description: ''
  name: profiles
  type: array
- description: ''
  name: persist
  type: array
- description: ''
  name: source
  type: string
- description: ''
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
  name: enabled
  type: boolean
- description: ''
  name: disabled
  type: boolean
- description: ''
  name: mirror
  type: string
- description: ''
  name: rateLimit
  type: string
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
- description: ''
  name: fallbackPersistence
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-virtual-server-update-schema.json
slug: bigip-icontrol-rest-virtual-server-update
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
title: VirtualServerUpdate
---
