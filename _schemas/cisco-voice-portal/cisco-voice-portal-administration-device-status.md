---
description: ''
layout: schema
name: DeviceStatus
properties_list:
- description: ''
  name: deviceId
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: services
  type: array
- description: CPU usage percentage
  name: cpuUsage
  type: number
- description: Memory usage percentage
  name: memoryUsage
  type: number
- description: Number of active calls on this device
  name: activeCalls
  type: integer
- description: ''
  name: timestamp
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-administration-device-status-schema.json
slug: cisco-voice-portal-administration-device-status
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: DeviceStatus
---
