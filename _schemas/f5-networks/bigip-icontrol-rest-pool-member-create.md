---
description: Request body for adding a new pool member.
layout: schema
name: PoolMemberCreate
properties_list:
- description: Member name in address:port format. If a node with the address does not exist, one will be created.
  name: name
  type: string
- description: IP address if it differs from the name.
  name: address
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
  name: priorityGroup
  type: integer
- description: ''
  name: rateLimit
  type: string
- description: ''
  name: ratio
  type: integer
- description: ''
  name: session
  type: string
- description: ''
  name: state
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-pool-member-create-schema.json
slug: bigip-icontrol-rest-pool-member-create
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
title: PoolMemberCreate
---
