---
description: ''
layout: schema
name: Device
properties_list:
- description: Unique identifier for the device
  name: deviceId
  type: string
- description: Hostname of the device
  name: hostname
  type: string
- description: IP address of the device
  name: ipAddress
  type: string
- description: Type of CVP component
  name: deviceType
  type: string
- description: Device description
  name: description
  type: string
- description: Current operational status
  name: status
  type: string
- description: Software version installed on the device
  name: version
  type: string
- description: Last time the OAMP server contacted this device
  name: lastContact
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-administration-device-schema.json
slug: cisco-voice-portal-administration-device
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: Device
---
