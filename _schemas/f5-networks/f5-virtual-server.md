---
description: Schema for an F5 BIG-IP LTM virtual server resource that directs client traffic to pools of backend servers based on IP address, port, and protocol configuration. Virtual servers are the core traffic management objects in the BIG-IP Local Traffic Manager.
layout: schema
name: F5 BIG-IP Virtual Server
properties_list:
- description: Resource type identifier for a virtual server.
  name: kind
  type: string
- description: Unique name of the virtual server resource within its partition.
  name: name
  type: string
- description: Full administrative path including partition (e.g., /Common/my_virtual).
  name: fullPath
  type: string
- description: Configuration generation counter incremented on each change.
  name: generation
  type: integer
- description: Self-referencing URI for this virtual server resource.
  name: selfLink
  type: string
- description: Whether the virtual contributes to the operational status of the associated virtual address.
  name: addressStatus
  type: string
- description: Automatic last hop setting controlling return traffic routing when the BIG-IP is not the default gateway.
  name: autoLasthop
  type: string
- description: Whether Clustered Multi-Processing (CMP) acceleration is enabled for this virtual server.
  name: cmpEnabled
  type: string
- description: Maximum number of concurrent connections allowed for this virtual server. A value of 0 means unlimited connections.
  name: connectionLimit
  type: integer
- description: User-defined description of the virtual server and its purpose.
  name: description
  type: string
- description: Destination IP address and service port the virtual server listens on, specified in /partition/address:port or /partition/address.port format.
  name: destination
  type: string
- description: When true, the virtual server does not accept new connections. Existing connections are maintained.
  name: disabled
  type: boolean
- description: When true, the virtual server accepts and processes client traffic.
  name: enabled
  type: boolean
- description: Persistence profile to use as a fallback when the primary persistence method fails to establish a session.
  name: fallbackPersistence
  type: string
- description: Score value used by the Global Traffic Manager for load balancing decisions across data centers.
  name: gtmScore
  type: integer
- description: Network protocol the virtual server handles.
  name: ipProtocol
  type: string
- description: Network mask for the destination address. Use 255.255.255.255 for a host-specific virtual server or a subnet mask for a network virtual server.
  name: mask
  type: string
- description: Whether connection and persistence state mirroring is enabled for high-availability failover scenarios.
  name: mirror
  type: string
- description: Whether NAT64 IPv6-to-IPv4 address translation is enabled.
  name: nat64
  type: string
- description: Administrative partition containing this virtual server resource.
  name: partition
  type: string
- description: Persistence profiles applied to the virtual server for maintaining session affinity.
  name: persist
  type: array
- description: Default pool that receives traffic from this virtual server, specified as a full partition-qualified path.
  name: pool
  type: string
- description: Traffic processing profiles applied to this virtual server (e.g., HTTP, TCP, SSL profiles).
  name: profiles
  type: array
- description: Maximum number of new connections per second. A value of 'disabled' or '0' means no rate limiting.
  name: rateLimit
  type: string
- description: Scope at which rate limiting is applied.
  name: rateLimitMode
  type: string
- description: Destination address mask bits used for rate limit tracking.
  name: rateLimitDstMask
  type: integer
- description: Source address mask bits used for rate limit tracking.
  name: rateLimitSrcMask
  type: integer
- description: iRules applied to this virtual server for custom traffic processing logic.
  name: rules
  type: array
- description: Source address filter. Only connections from this network are accepted by the virtual server.
  name: source
  type: string
- description: Source port translation behavior controlling how client source ports are handled.
  name: sourcePort
  type: string
- description: Current SYN Cookie DDoS protection status.
  name: synCookieStatus
  type: string
- description: Whether destination address translation is enabled. When enabled, the BIG-IP translates the destination address to the pool member address.
  name: translateAddress
  type: string
- description: Whether destination port translation is enabled. When enabled, the BIG-IP translates the destination port to the pool member port.
  name: translatePort
  type: string
- description: When true, the virtual server is enabled only on VLANs listed in the vlans property.
  name: vlansEnabled
  type: boolean
- description: When true, the virtual server is disabled on VLANs listed in the vlans property.
  name: vlansDisabled
  type: boolean
- description: List of VLANs on which the virtual server is enabled or disabled, depending on vlansEnabled/vlansDisabled setting.
  name: vlans
  type: array
- description: System-assigned index for the virtual server.
  name: vsIndex
  type: integer
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/f5-virtual-server-schema.json
slug: f5-virtual-server
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
title: F5 BIG-IP Virtual Server
---
