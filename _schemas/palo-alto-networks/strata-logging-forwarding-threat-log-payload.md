---
description: Schema for a forwarded PAN-OS threat log entry. Threat logs capture security events detected by the firewall's threat prevention engines, providing detailed information about malware, exploits, spyware, command-and-control traffic, and other detected threats.
layout: schema
name: ThreatLogPayload
properties_list:
- description: Timestamp when the threat log entry was received by Strata Logging Service.
  name: receive_time
  type: string
- description: Serial number of the Palo Alto Networks device that generated this threat log entry.
  name: serial
  type: string
- description: Log type identifier, always THREAT for threat log entries.
  name: type
  type: string
- description: Threat log subtype indicating which threat prevention engine or signature category generated the detection event.
  name: subtype
  type: string
- description: Source IP address of the session in which the threat was detected.
  name: src
  type: string
- description: Destination IP address of the session in which the threat was detected.
  name: dst
  type: string
- description: Source port number of the session.
  name: sport
  type: integer
- description: Destination port number of the session.
  name: dport
  type: integer
- description: IP protocol of the session.
  name: proto
  type: string
- description: Application identified by App-ID in the threat session.
  name: app
  type: string
- description: Name of the detected threat as defined in the Palo Alto Networks threat database and threat vault.
  name: threat_name
  type: string
- description: Severity level of the detected threat as defined by the threat signature or detection engine.
  name: severity
  type: string
- description: Action taken by the threat prevention engine in response to the detected threat.
  name: action
  type: string
- description: Direction of the detected attack relative to the network session flow.
  name: direction
  type: string
- description: Unique numeric identifier for the threat signature from the Palo Alto Networks threat vault. Used for threat intelligence lookup and signature reference.
  name: threat_id
  type: string
- description: Name of the security policy rule that matched the session in which the threat was detected.
  name: rule_name
  type: string
- description: Source security zone of the threat session.
  name: src_zone
  type: string
- description: Destination security zone of the threat session.
  name: dst_zone
  type: string
- description: Source user identity if User-ID is enabled.
  name: src_user
  type: string
- description: URL or filename associated with the detected threat, depending on the threat subtype.
  name: url_or_filename
  type: string
- description: Hostname of the firewall that generated this threat log entry.
  name: device_name
  type: string
- description: Virtual system name or identifier on the firewall.
  name: vsys
  type: string
- description: Name of the log forwarding profile that forwarded this log entry.
  name: log_forwarding_profile
  type: string
- description: Output format in which this log entry was forwarded.
  name: output_format
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-forwarding-threat-log-payload-schema.json
slug: strata-logging-forwarding-threat-log-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ThreatLogPayload
---
