---
description: Request body for creating a new node.
layout: schema
name: NodeCreate
properties_list:
- description: Name of the node. If the name is an IP address, the address property is optional.
  name: name
  type: string
- description: IP address of the node. Required if the name is not an IP address.
  name: address
  type: string
- description: ''
  name: partition
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: connectionLimit
  type: integer
- description: ''
  name: monitor
  type: string
- description: ''
  name: rateLimit
  type: string
- description: ''
  name: ratio
  type: integer
- description: ''
  name: fqdn
  type: object
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-node-create-schema.json
slug: bigip-icontrol-rest-node-create
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
title: NodeCreate
---
