---
description: A pool resource that contains a group of backend server members used for load balancing traffic from virtual servers.
layout: schema
name: Pool
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Name of the pool resource.
  name: name
  type: string
- description: Full path including partition.
  name: fullPath
  type: string
- description: Configuration generation counter.
  name: generation
  type: integer
- description: Self-referencing URI.
  name: selfLink
  type: string
- description: Whether the pool can load balance NAT connections.
  name: allowNat
  type: string
- description: Whether the pool can load balance SNAT connections.
  name: allowSnat
  type: string
- description: User-defined description.
  name: description
  type: string
- description: Whether to ignore persisted weight when calculating load distribution.
  name: ignorePersistedWeight
  type: string
- description: Type of Service level for client-bound outgoing packets.
  name: ipTosToClient
  type: string
- description: Type of Service level for server-bound outgoing packets.
  name: ipTosToServer
  type: string
- description: QoS level for outgoing packets to clients.
  name: linkQosToClient
  type: string
- description: QoS level for outgoing packets to servers.
  name: linkQosToServer
  type: string
- description: Load balancing algorithm used to distribute traffic.
  name: loadBalancingMode
  type: string
- description: Minimum number of active members for priority-group activation.
  name: minActiveMembers
  type: integer
- description: Minimum number of operational pool members required before action is taken.
  name: minUpMembers
  type: integer
- description: Action to take when the number of operational members falls below the minimum.
  name: minUpMembersAction
  type: string
- description: Whether minimum member monitoring is enabled.
  name: minUpMembersChecking
  type: string
- description: Health monitor or monitor rule applied to pool members. Specify multiple monitors with 'and' or 'min N of'.
  name: monitor
  type: string
- description: Administrative partition.
  name: partition
  type: string
- description: Maximum number of connections queued per member.
  name: queueDepthLimit
  type: integer
- description: Whether to queue connections when limits are reached.
  name: queueOnConnectionLimit
  type: string
- description: Maximum time in milliseconds a connection can remain queued.
  name: queueTimeLimit
  type: integer
- description: Number of reselection attempts after a passive failure.
  name: reselectTries
  type: integer
- description: Action to take when all pool members are unavailable.
  name: serviceDownAction
  type: string
- description: Time in seconds to gradually increase traffic to a newly enabled member.
  name: slowRampTime
  type: integer
- description: Reference to the pool members subcollection.
  name: membersReference
  type: object
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-pool-schema.json
slug: bigip-icontrol-rest-pool
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
title: Pool
---
