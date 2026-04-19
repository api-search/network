---
description: ''
layout: schema
name: CallDetailRecord
properties_list:
- description: Globally unique call identifier
  name: callGuid
  type: string
- description: Call start timestamp
  name: callStartTime
  type: string
- description: Call end timestamp
  name: callEndTime
  type: string
- description: Caller ANI (Automatic Number Identification)
  name: callingNumber
  type: string
- description: Called DNIS (Dialed Number Identification Service)
  name: calledNumber
  type: string
- description: Final call outcome
  name: callResult
  type: string
- description: Total call duration in seconds
  name: callDuration
  type: integer
- description: Duration of self-service (IVR) portion in seconds
  name: selfServiceDuration
  type: integer
- description: Duration in queue in seconds
  name: queueDuration
  type: integer
- description: VXML application that handled the call
  name: applicationName
  type: string
- description: Call Server that processed the call
  name: callServerHostname
  type: string
- description: VXML Server that executed the application
  name: vxmlServerHostname
  type: string
- description: SIP Call-ID header value
  name: sipCallId
  type: string
- description: ICM/UCCE call key for correlation
  name: icmCallKey
  type: string
- description: Expanded Call Context (ECC) variables
  name: eccVariables
  type: object
- description: Transfer destination number if the call was transferred
  name: transferDestination
  type: string
- description: Error code if the call ended in error
  name: errorCode
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-reporting-call-detail-record-schema.json
slug: cisco-voice-portal-reporting-call-detail-record
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: CallDetailRecord
---
