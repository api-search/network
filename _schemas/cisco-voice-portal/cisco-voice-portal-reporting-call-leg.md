---
description: ''
layout: schema
name: CallLeg
properties_list:
- description: ''
  name: legId
  type: string
- description: ''
  name: callGuid
  type: string
- description: Type of call leg
  name: legType
  type: string
- description: ''
  name: startTime
  type: string
- description: ''
  name: endTime
  type: string
- description: Leg duration in seconds
  name: duration
  type: integer
- description: SIP From URI
  name: fromUri
  type: string
- description: SIP To URI
  name: toUri
  type: string
- description: Server that handled this leg
  name: serverHostname
  type: string
- description: Final SIP response code for this leg
  name: sipResponseCode
  type: integer
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-reporting-call-leg-schema.json
slug: cisco-voice-portal-reporting-call-leg
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: CallLeg
---
