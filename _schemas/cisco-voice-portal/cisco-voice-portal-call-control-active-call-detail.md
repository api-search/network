---
description: ''
layout: schema
name: ActiveCallDetail
properties_list:
- description: ''
  name: callGuid
  type: string
- description: ''
  name: state
  type: string
- description: ''
  name: callingNumber
  type: string
- description: ''
  name: calledNumber
  type: string
- description: ''
  name: startTime
  type: string
- description: ''
  name: duration
  type: integer
- description: ''
  name: applicationName
  type: string
- description: SIP Call-ID
  name: sipCallId
  type: string
- description: ''
  name: sipFromTag
  type: string
- description: ''
  name: sipToTag
  type: string
- description: ''
  name: icmRouteResult
  type: object
- description: VXML Server currently handling the call
  name: vxmlServer
  type: string
- description: Chronological list of call events
  name: callHistory
  type: array
- description: ''
  name: eccVariables
  type: object
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-call-control-active-call-detail-schema.json
slug: cisco-voice-portal-call-control-active-call-detail
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: ActiveCallDetail
---
