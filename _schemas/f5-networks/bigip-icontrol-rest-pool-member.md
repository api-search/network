---
description: A pool member resource representing an individual backend server within a pool, identified by address and port.
layout: schema
name: PoolMember
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Member name in address:port format.
  name: name
  type: string
- description: Full path including partition.
  name: fullPath
  type: string
- description: ''
  name: generation
  type: integer
- description: ''
  name: selfLink
  type: string
- description: IP address of the pool member.
  name: address
  type: string
- description: Maximum concurrent connections. 0 means unlimited.
  name: connectionLimit
  type: integer
- description: User-defined description.
  name: description
  type: string
- description: Dynamic ratio for load balancing.
  name: dynamicRatio
  type: integer
- description: Whether this is a transient auto-discovered member.
  name: ephemeral
  type: string
- description: Whether the member inherits the encapsulation profile from its parent pool.
  name: inheritProfile
  type: string
- description: Whether monitor actions are logged.
  name: logging
  type: string
- description: Health monitor override for this member.
  name: monitor
  type: string
- description: Administrative partition.
  name: partition
  type: string
- description: Priority group number. Higher values receive traffic first when priority-group activation is configured.
  name: priorityGroup
  type: integer
- description: Maximum connections per second. disabled means no limit.
  name: rateLimit
  type: string
- description: Ratio weight for load balancing.
  name: ratio
  type: integer
- description: Session availability state.
  name: session
  type: string
- description: Operational state of the member.
  name: state
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-pool-member-schema.json
slug: bigip-icontrol-rest-pool-member
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
title: PoolMember
---
