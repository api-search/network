---
description: ''
layout: schema
name: VxmlSessionDetail
properties_list:
- description: ''
  name: sessionId
  type: string
- description: ''
  name: callGuid
  type: string
- description: ''
  name: applicationName
  type: string
- description: ''
  name: startTime
  type: string
- description: ''
  name: duration
  type: integer
- description: ''
  name: currentElement
  type: string
- description: ''
  name: callingNumber
  type: string
- description: ''
  name: calledNumber
  type: string
- description: VXML session-level variables
  name: sessionVariables
  type: object
- description: History of elements visited in this session
  name: elementHistory
  type: array
- description: Last input received from the caller (DTMF or ASR result)
  name: lastUserInput
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-vxml-services-vxml-session-detail-schema.json
slug: cisco-voice-portal-vxml-services-vxml-session-detail
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: VxmlSessionDetail
---
