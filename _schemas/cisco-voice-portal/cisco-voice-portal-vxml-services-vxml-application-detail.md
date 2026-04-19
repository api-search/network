---
description: ''
layout: schema
name: VxmlApplicationDetail
properties_list:
- description: ''
  name: applicationName
  type: string
- description: ''
  name: applicationType
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: version
  type: string
- description: ''
  name: activeSessions
  type: integer
- description: ''
  name: deployedAt
  type: string
- description: ''
  name: description
  type: string
- description: Starting element of the call flow
  name: entryPoint
  type: string
- description: List of element names in the application
  name: elements
  type: array
- description: Path to the application media files
  name: mediaDirectory
  type: string
- description: Path to the application grammar files
  name: grammarDirectory
  type: string
- description: Application-level configuration parameters
  name: configParameters
  type: object
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-vxml-services-vxml-application-detail-schema.json
slug: cisco-voice-portal-vxml-services-vxml-application-detail
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: VxmlApplicationDetail
---
