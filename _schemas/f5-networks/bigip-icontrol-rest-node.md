---
description: A node resource representing an individual backend server by its IP address or FQDN. Nodes are automatically created when pool members are added, or can be created independently.
layout: schema
name: Node
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Name of the node (typically the IP address).
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
- description: IP address of the node.
  name: address
  type: string
- description: Maximum concurrent connections. 0 means unlimited.
  name: connectionLimit
  type: integer
- description: User-defined description.
  name: description
  type: string
- description: Dynamic ratio weight for load balancing.
  name: dynamicRatio
  type: integer
- description: Whether this is a transient auto-discovered node.
  name: ephemeral
  type: string
- description: FQDN configuration for DNS-based node resolution.
  name: fqdn
  type: object
- description: Whether monitor actions are logged.
  name: logging
  type: string
- description: Health monitor applied to the node.
  name: monitor
  type: string
- description: Administrative partition.
  name: partition
  type: string
- description: Maximum connections per second. 0 means no limit.
  name: rateLimit
  type: string
- description: Fixed ratio weight for load balancing.
  name: ratio
  type: integer
- description: Session availability state.
  name: session
  type: string
- description: Operational state of the node.
  name: state
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-node-schema.json
slug: bigip-icontrol-rest-node
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
title: Node
---
