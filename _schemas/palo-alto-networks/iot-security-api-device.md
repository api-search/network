---
description: Device schema from Palo Alto Networks IoT Security API
layout: schema
name: Device
properties_list:
- description: Unique device identifier.
  name: deviceid
  type: string
- description: IPv4 address of the device.
  name: ip
  type: string
- description: MAC address of the device.
  name: mac
  type: string
- description: Hostname or NetBIOS name of the device.
  name: hostname
  type: string
- description: Device profile classification (e.g., IP Camera, Infusion Pump).
  name: profile
  type: string
- description: Device category (e.g., IoT, OT, IT).
  name: category
  type: string
- description: Aggregate risk score from 0 (lowest) to 100 (highest).
  name: risk_score
  type: integer
- description: Detected operating system.
  name: os
  type: string
- description: Detected operating system version.
  name: os_version
  type: string
- description: Device manufacturer or vendor.
  name: vendor
  type: string
- description: Device model identifier.
  name: model
  type: string
- description: Network site where the device was discovered.
  name: site
  type: string
- description: Subnet the device belongs to.
  name: subnet
  type: string
- description: Timestamp when the device was first discovered.
  name: first_seen
  type: string
- description: Timestamp when the device was last active.
  name: last_seen
  type: string
- description: Whether the device is currently monitored.
  name: monitored
  type: string
- description: Confidence level of the device profile classification.
  name: confidence_score
  type: integer
- description: User-defined or system-assigned tags.
  name: tags
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/iot-security-api-device-schema.json
slug: iot-security-api-device
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Device
---
