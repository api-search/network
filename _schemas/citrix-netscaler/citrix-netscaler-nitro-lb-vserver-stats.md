---
description: Performance and health statistics for a load balancing virtual server, including connection metrics, throughput, error rates, and APDEX scores.
layout: schema
name: LbVserverStats
properties_list:
- description: Name of the load balancing virtual server.
  name: name
  type: string
- description: IP address of the virtual server.
  name: primaryipaddress
  type: string
- description: Port number of the virtual server.
  name: primaryport
  type: integer
- description: Protocol type of the virtual server.
  name: type
  type: string
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
- description: Number of active persistence sessions.
  name: curpersistencesessions
  type: number
- description: Percentage of UP services bound to this virtual server.
  name: vslbhealth
  type: number
- description: Number of active (UP) services.
  name: actsvcs
  type: number
- description: Number of inactive (DOWN) services.
  name: inactsvcs
  type: number
- description: Total number of virtual server hits since last restart.
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
- description: Total number of request bytes received.
  name: totalrequestbytes
  type: number
- description: Rate of request bytes per second.
  name: requestbytesrate
  type: number
- description: Total number of response bytes sent.
  name: totalresponsebytes
  type: number
- description: Rate of response bytes per second.
  name: responsebytesrate
  type: number
- description: Total packets received.
  name: totalpktsrecvd
  type: number
- description: Rate of packets received per second.
  name: pktsrecvdrate
  type: number
- description: Total packets sent.
  name: totalpktssent
  type: number
- description: Rate of packets sent per second.
  name: pktssentrate
  type: number
- description: Total server busy errors.
  name: totalsvrbusyerr
  type: number
- description: Rate of server busy errors per second.
  name: svrbusyerrrate
  type: number
- description: Number of requests in the surge queue.
  name: surgecount
  type: number
- description: Total number of spillover events.
  name: totspillovers
  type: number
- description: Total diversions to the backup virtual server.
  name: totvserverdownbackuphits
  type: number
- description: Average client time-to-last-byte in microseconds.
  name: avgcltttlb
  type: number
- description: APDEX score based on client response times (0.0-1.0).
  name: cltresponsetimeapdex
  type: number
- description: CPU utilization in parts per million.
  name: cpuusagepm
  type: number
- description: Total HTTP/2 requests received.
  name: totalh2requests
  type: number
- description: Rate of HTTP/2 requests per second.
  name: h2requestsrate
  type: number
- description: Total HTTP/2 responses sent.
  name: totalh2responses
  type: number
- description: Rate of HTTP/2 responses per second.
  name: h2responsesrate
  type: number
- description: Total invalid request/response count.
  name: invalidrequestresponse
  type: number
- description: Total dropped invalid request/response count.
  name: invalidrequestresponsedropped
  type: number
- description: Configured spillover threshold.
  name: sothreshold
  type: number
- description: Total request retry count.
  name: reqretrycount
  type: number
- description: Times retry count was exceeded.
  name: reqretrycountexceeded
  type: number
- description: Number of deferred requests.
  name: deferredreq
  type: number
- description: Rate of deferred requests per second.
  name: deferredreqrate
  type: number
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-lb-vserver-stats-schema.json
slug: citrix-netscaler-nitro-lb-vserver-stats
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: LbVserverStats
---
