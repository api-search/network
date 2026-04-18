---
description: Request body for updating a pool.
layout: schema
name: PoolUpdate
properties_list:
- description: ''
  name: description
  type: string
- description: ''
  name: loadBalancingMode
  type: string
- description: ''
  name: monitor
  type: string
- description: ''
  name: serviceDownAction
  type: string
- description: ''
  name: slowRampTime
  type: integer
- description: ''
  name: minActiveMembers
  type: integer
- description: ''
  name: allowNat
  type: string
- description: ''
  name: allowSnat
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-pool-update-schema.json
slug: bigip-icontrol-rest-pool-update
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
title: PoolUpdate
---
