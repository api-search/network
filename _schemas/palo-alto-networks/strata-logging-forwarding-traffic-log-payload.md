---
description: Schema for a forwarded PAN-OS traffic log entry. Traffic logs capture session metadata for every network connection processed by the firewall, providing comprehensive network visibility for security operations, compliance, and analytics.
layout: schema
name: TrafficLogPayload
properties_list:
- description: Timestamp when the log entry was received by Strata Logging Service from the generating firewall device.
  name: receive_time
  type: string
- description: Serial number of the Palo Alto Networks firewall or Prisma Access node that generated this log entry.
  name: serial
  type: string
- description: Log type identifier, always TRAFFIC for traffic log entries.
  name: type
  type: string
- description: Traffic log subtype indicating what session lifecycle event triggered this log entry.
  name: subtype
  type: string
- description: Source IP address of the network session.
  name: src
  type: string
- description: Destination IP address of the network session.
  name: dst
  type: string
- description: Source port number of the network session.
  name: sport
  type: integer
- description: Destination port number of the network session.
  name: dport
  type: integer
- description: IP protocol name or number for the session (e.g., tcp, udp, icmp).
  name: proto
  type: string
- description: Application identified by PAN-OS App-ID, such as ssl, web-browsing, dns, or a specific SaaS application name.
  name: app
  type: string
- description: Enforcement action applied to the session by the matching security policy rule.
  name: action
  type: string
- description: Total bytes sent from client to server in this session.
  name: bytes_sent
  type: integer
- description: Total bytes received by client from server in this session.
  name: bytes_received
  type: integer
- description: Unique session identifier assigned by the firewall for this network session.
  name: session_id
  type: string
- description: Name of the security policy rule that matched and processed this session.
  name: rule_name
  type: string
- description: Source security zone from which the session originated.
  name: src_zone
  type: string
- description: Destination security zone to which the session is destined.
  name: dst_zone
  type: string
- description: Source user identity associated with the session if User-ID is enabled on the ingress zone.
  name: src_user
  type: string
- description: Destination user identity if available.
  name: dst_user
  type: string
- description: Post-NAT source IP address after address translation.
  name: nat_src
  type: string
- description: Post-NAT destination IP address after address translation.
  name: nat_dst
  type: string
- description: Post-NAT source port after port address translation.
  name: nat_sport
  type: integer
- description: Post-NAT destination port after port address translation.
  name: nat_dport
  type: integer
- description: Total packets sent from client in this session.
  name: packets_sent
  type: integer
- description: Total packets received by client in this session.
  name: packets_received
  type: integer
- description: Total session duration in seconds.
  name: session_duration
  type: integer
- description: Hostname of the firewall that generated this log entry.
  name: device_name
  type: string
- description: Virtual system name or identifier on the firewall.
  name: vsys
  type: string
- description: Name of the Strata Logging Service log forwarding profile that forwarded this log entry.
  name: log_forwarding_profile
  type: string
- description: Output format in which this log entry was forwarded to the destination.
  name: output_format
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-forwarding-traffic-log-payload-schema.json
slug: strata-logging-forwarding-traffic-log-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TrafficLogPayload
---
