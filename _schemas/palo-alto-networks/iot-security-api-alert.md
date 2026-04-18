---
description: Alert schema from Palo Alto Networks IoT Security API
layout: schema
name: Alert
properties_list:
- description: Unique alert identifier.
  name: id
  type: string
- description: Alert type classification.
  name: type
  type: string
- description: Alert severity level.
  name: severity
  type: string
- description: Human-readable alert description.
  name: description
  type: string
- description: Identifier of the affected device.
  name: deviceid
  type: string
- description: IP address of the affected device.
  name: device_ip
  type: string
- description: Profile of the affected device.
  name: device_profile
  type: string
- description: Whether the alert has been resolved.
  name: resolved
  type: string
- description: Resolution reason if resolved.
  name: resolved_reason
  type: string
- description: Timestamp when the alert was generated.
  name: timestamp
  type: string
- description: Additional alert-specific details.
  name: details
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/iot-security-api-alert-schema.json
slug: iot-security-api-alert
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Alert
---
