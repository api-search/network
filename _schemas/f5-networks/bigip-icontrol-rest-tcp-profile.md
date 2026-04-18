---
description: A TCP profile that defines how the BIG-IP processes TCP traffic, including connection settings, timeouts, and optimization.
layout: schema
name: TcpProfile
properties_list:
- description: ''
  name: kind
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: fullPath
  type: string
- description: ''
  name: generation
  type: integer
- description: ''
  name: selfLink
  type: string
- description: Whether Appropriate Byte Counting is enabled.
  name: abc
  type: string
- description: Whether to send ACK on PUSH flag.
  name: ackOnPush
  type: string
- description: Timeout in seconds for CLOSE-WAIT state.
  name: closeWaitTimeout
  type: integer
- description: TCP congestion control algorithm.
  name: congestionControl
  type: string
- description: Parent profile.
  name: defaultsFrom
  type: string
- description: Whether to defer connection acceptance.
  name: deferredAccept
  type: string
- description: ''
  name: description
  type: string
- description: Timeout in seconds for FIN-WAIT state.
  name: finWaitTimeout
  type: integer
- description: Idle timeout in seconds. Connections idle longer than this value are closed.
  name: idleTimeout
  type: integer
- description: Initial TCP congestion window size.
  name: initCwnd
  type: integer
- description: Initial TCP receive window size.
  name: initRwnd
  type: integer
- description: Interval in seconds between TCP keep-alive probes.
  name: keepAliveInterval
  type: integer
- description: Maximum number of TCP retransmission attempts.
  name: maxRetrans
  type: integer
- description: Maximum segment size (MSS) in bytes.
  name: maxSegmentSize
  type: integer
- description: Nagle algorithm setting.
  name: nagle
  type: string
- description: TCP receive window size in bytes.
  name: receiveWindowSize
  type: integer
- description: TCP send buffer size in bytes.
  name: sendBufferSize
  type: integer
- description: Maximum SYN retransmission attempts.
  name: synMaxRetrans
  type: integer
- description: Whether to recycle TIME-WAIT connections.
  name: timeWaitRecycle
  type: string
- description: Timeout in milliseconds for TIME-WAIT state.
  name: timeWaitTimeout
  type: integer
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-tcp-profile-schema.json
slug: bigip-icontrol-rest-tcp-profile
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
title: TcpProfile
---
