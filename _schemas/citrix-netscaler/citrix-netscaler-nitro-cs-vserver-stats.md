---
description: Performance statistics for a content switching virtual server.
layout: schema
name: CsVserverStats
properties_list:
- description: Name of the content switching virtual server.
  name: name
  type: string
- description: IP address of the virtual server.
  name: primaryipaddress
  type: string
- description: Port number of the virtual server.
  name: primaryport
  type: integer
- description: Current operational state.
  name: state
  type: string
- description: Number of current client connections.
  name: curclntconnections
  type: number
- description: Number of current server connections.
  name: cursrvrconnections
  type: number
- description: Number of connections in ESTABLISHED state.
  name: establishedconn
  type: number
- description: Total number of virtual server hits.
  name: tothits
  type: number
- description: Rate of hits per second.
  name: hitsrate
  type: number
- description: Total number of requests received.
  name: totalrequests
  type: number
- description: Rate of requests per second.
  name: requestsrate
  type: number
- description: Total number of responses sent.
  name: totalresponses
  type: number
- description: Rate of responses per second.
  name: responsesrate
  type: number
- description: Total bytes of requests received.
  name: totalrequestbytes
  type: number
- description: Total bytes of responses sent.
  name: totalresponsebytes
  type: number
- description: Total packets received.
  name: totalpktsrecvd
  type: number
- description: Total packets sent.
  name: totalpktssent
  type: number
- description: Total spillover events.
  name: totspillovers
  type: number
- description: Total labeled connections.
  name: labelledconn
  type: number
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-cs-vserver-stats-schema.json
slug: citrix-netscaler-nitro-cs-vserver-stats
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: CsVserverStats
---
