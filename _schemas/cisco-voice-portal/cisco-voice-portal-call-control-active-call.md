---
description: ''
layout: schema
name: ActiveCall
properties_list:
- description: Globally unique call identifier
  name: callGuid
  type: string
- description: ''
  name: state
  type: string
- description: Caller ANI
  name: callingNumber
  type: string
- description: Called DNIS
  name: calledNumber
  type: string
- description: ''
  name: startTime
  type: string
- description: Current call duration in seconds
  name: duration
  type: integer
- description: Current VXML application handling the call
  name: applicationName
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-call-control-active-call-schema.json
slug: cisco-voice-portal-call-control-active-call
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: ActiveCall
---
