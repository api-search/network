---
description: Schema for a CVP managed device. Devices are the server components that make up a CVP deployment, including Call Servers, VXML Servers, Reporting Servers, and Media Servers. Devices are registered with and managed through the CVP OAMP Server.
layout: schema
name: Cisco Voice Portal Device
properties_list:
- description: Unique identifier for the device assigned by the OAMP Server
  name: deviceId
  type: string
- description: Fully qualified hostname of the device
  name: hostname
  type: string
- description: IPv4 address of the device
  name: ipAddress
  type: string
- description: Type of CVP server component
  name: deviceType
  type: string
- description: Administrator-defined description of the device
  name: description
  type: string
- description: Current operational status
  name: status
  type: string
- description: Installed CVP software version
  name: version
  type: string
- description: Timestamp of the last successful communication with the device
  name: lastContact
  type: string
- description: Services running on the device
  name: services
  type: array
- description: ''
  name: resourceUtilization
  type: object
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-device.json
slug: cisco-voice-portal-device
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: Cisco Voice Portal Device
---
