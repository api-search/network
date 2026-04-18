---
description: A virtual server resource that directs client traffic to a pool of backend servers based on an IP address and port combination.
layout: schema
name: VirtualServer
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Name of the virtual server resource.
  name: name
  type: string
- description: Full path including partition.
  name: fullPath
  type: string
- description: Configuration generation counter.
  name: generation
  type: integer
- description: Self-referencing URI for this resource.
  name: selfLink
  type: string
- description: Whether the virtual contributes to the operational status of the associated virtual address.
  name: addressStatus
  type: string
- description: Automatic last hop setting for return traffic routing.
  name: autoLasthop
  type: string
- description: Whether Clustered Multi-Processing (CMP) acceleration is enabled.
  name: cmpEnabled
  type: string
- description: Maximum number of concurrent connections allowed. A value of 0 means unlimited.
  name: connectionLimit
  type: integer
- description: User-defined description of the virtual server.
  name: description
  type: string
- description: Destination IP address and service port in the format /partition/address:port or /partition/address.port.
  name: destination
  type: string
- description: When true, the virtual server does not accept new connections.
  name: disabled
  type: boolean
- description: When true, the virtual server accepts and processes traffic.
  name: enabled
  type: boolean
- description: Persistence profile to use when the primary persistence method fails.
  name: fallbackPersistence
  type: string
- description: Score value used by Global Traffic Manager for load balancing decisions.
  name: gtmScore
  type: integer
- description: IP protocol for the virtual server.
  name: ipProtocol
  type: string
- description: Network mask for the destination address. Use 255.255.255.255 for host-specific virtual servers.
  name: mask
  type: string
- description: Whether connection and persistence mirroring is enabled for high availability failover.
  name: mirror
  type: string
- description: Whether NAT64 translation is enabled.
  name: nat64
  type: string
- description: Administrative partition containing this resource.
  name: partition
  type: string
- description: Persistence profiles applied to the virtual server.
  name: persist
  type: array
- description: Default pool for directing traffic. Specified as a full path (e.g., /Common/my_pool).
  name: pool
  type: string
- description: Profiles applied to the virtual server.
  name: profiles
  type: array
- description: Maximum number of connections per second. A value of disabled or 0 means no limit.
  name: rateLimit
  type: string
- description: Scope of rate limiting.
  name: rateLimitMode
  type: string
- description: iRules applied to the virtual server.
  name: rules
  type: array
- description: Source address filter. Only connections from this network are accepted.
  name: source
  type: string
- description: Source port translation behavior.
  name: sourcePort
  type: string
- description: Current SYN Cookie protection status.
  name: synCookieStatus
  type: string
- description: Whether address translation is enabled.
  name: translateAddress
  type: string
- description: Whether port translation is enabled.
  name: translatePort
  type: string
- description: Whether VLAN filtering is enabled.
  name: vlansEnabled
  type: boolean
- description: Whether the virtual server is disabled on listed VLANs.
  name: vlansDisabled
  type: boolean
- description: List of VLANs on which the virtual server is enabled or disabled.
  name: vlans
  type: array
- description: System-assigned index for the virtual server.
  name: vsIndex
  type: integer
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-virtual-server-schema.json
slug: bigip-icontrol-rest-virtual-server
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
title: VirtualServer
---
