---
description: A content switching virtual server that directs client requests to different load balancing virtual servers based on content switching policies evaluating request attributes such as URL, HTTP header, or source IP address.
layout: schema
name: CsVserver
properties_list:
- description: Name for the content switching virtual server. Must be unique and begin with a letter, number, or underscore. Maximum 127 characters.
  name: name
  type: string
- description: Traffic domain identifier. Range 0-4094.
  name: td
  type: integer
- description: Protocol of the service running on the virtual server.
  name: servicetype
  type: string
- description: IPv4 or IPv6 address of the content switching virtual server.
  name: ipv46
  type: string
- description: Port number on which the content switching virtual server listens.
  name: port
  type: integer
- description: Name of the IP set to bind to the virtual server.
  name: ipset
  type: string
- description: Number of consecutive IP addresses for the virtual server. Range 2-254.
  name: range
  type: integer
- description: IP address pattern for matching incoming requests.
  name: ippattern
  type: string
- description: IP mask applied with ippattern to form an address range.
  name: ipmask
  type: string
- description: Whether the virtual server checks the backend server state for updates.
  name: stateupdate
  type: string
- description: Type of precedence for content switching policies. RULE means policies are evaluated in priority order. URL means URL-based switching takes precedence.
  name: precedence
  type: string
- description: Whether URL-based content switching is case sensitive.
  name: casesensitive
  type: string
- description: Spillover method for the content switching virtual server.
  name: somethod
  type: string
- description: Whether to maintain persistence during spillover.
  name: sopersistence
  type: string
- description: Persistence timeout in minutes during spillover. Range 2-1440.
  name: sopersistencetimeout
  type: integer
- description: Threshold value for the spillover method.
  name: sothreshold
  type: integer
- description: URL to redirect requests to when the virtual server is DOWN.
  name: redirecturl
  type: string
- description: Client idle timeout in seconds. Range 0-31536000.
  name: clttimeout
  type: integer
- description: Flush all active transactions when the virtual server goes DOWN.
  name: downstateflush
  type: string
- description: Insert the virtual server VIP address and port into the HTTP header of the request.
  name: insertvserveripport
  type: string
- description: Name of the HTTP header in which the VIP is inserted.
  name: vipheader
  type: string
- description: Continue to direct traffic to the virtual server even when DOWN in HA mode.
  name: disableprimaryondown
  type: string
- description: Whether authentication is enabled for the virtual server.
  name: authentication
  type: string
- description: FQDN of the authentication virtual server.
  name: authenticationhost
  type: string
- description: Whether HTTP 401-based authentication is enabled.
  name: authn401
  type: string
- description: Name of the authentication virtual server.
  name: authnvsname
  type: string
- description: Whether push functionality is enabled.
  name: push
  type: string
- description: Expression for extracting a label from the request.
  name: pushlabel
  type: string
- description: Allow multiple clients to connect to the push vserver.
  name: pushmulticlients
  type: string
- description: Description or comments about the content switching virtual server.
  name: comment
  type: string
- description: Whether Layer 2 connectivity is enabled between the client and server.
  name: l2conn
  type: string
- description: How the appliance responds to ICMP ping requests for the VIP.
  name: icmpvsrresponse
  type: string
- description: Route health injection state for the virtual server.
  name: rhistate
  type: string
- description: Whether to log AppFlow records for the virtual server.
  name: appflowlog
  type: string
- description: Administrative state of the virtual server.
  name: state
  type: string
- description: Name of the default load balancing virtual server bound to this content switching virtual server. Requests that do not match any policy are sent here.
  name: lbvserver
  type: string
- description: Name of the target load balancing virtual server to which content is switched.
  name: targetlbvserver
  type: string
- description: Cache type for integrated caching.
  name: cachetype
  type: string
- description: Type of cache redirect for the virtual server.
  name: redirect
  type: string
- description: Current operational state of the virtual server.
  name: curstate
  type: string
- description: Current status of the virtual server. 1 indicates UP.
  name: status
  type: integer
- description: Time when the virtual server state last changed.
  name: statechangetimesec
  type: string
- description: Number of ticks since the last state change.
  name: tickssincelaststatechange
  type: integer
- description: Virtual server type (e.g., content-based or IP-address based).
  name: type
  type: string
- description: Node group name to which the virtual server is bound.
  name: ngname
  type: string
- description: The value of the IP address, based on the virtual server type.
  name: value
  type: string
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-cs-vserver-schema.json
slug: citrix-netscaler-nitro-cs-vserver
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: CsVserver
---
