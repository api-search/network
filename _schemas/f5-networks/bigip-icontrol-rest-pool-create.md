---
description: Request body for creating a new pool.
layout: schema
name: PoolCreate
properties_list:
- description: Name of the pool.
  name: name
  type: string
- description: Administrative partition.
  name: partition
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: loadBalancingMode
  type: string
- description: ''
  name: monitor
  type: string
- description: Initial pool members to add during creation.
  name: members
  type: array
- description: ''
  name: serviceDownAction
  type: string
- description: ''
  name: slowRampTime
  type: integer
- description: ''
  name: allowNat
  type: string
- description: ''
  name: allowSnat
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-pool-create-schema.json
slug: bigip-icontrol-rest-pool-create
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
title: PoolCreate
---
