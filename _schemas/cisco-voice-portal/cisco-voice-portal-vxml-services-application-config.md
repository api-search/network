---
description: ''
layout: schema
name: ApplicationConfig
properties_list:
- description: ''
  name: applicationName
  type: string
- description: Runtime configuration parameters
  name: parameters
  type: object
- description: ''
  name: defaultLanguage
  type: string
- description: VXML document fetch timeout in milliseconds
  name: fetchTimeout
  type: integer
- description: Maximum session duration in seconds
  name: maxSessionDuration
  type: integer
- description: Allowed input modes
  name: inputModes
  type: array
- description: ''
  name: loggingLevel
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-vxml-services-application-config-schema.json
slug: cisco-voice-portal-vxml-services-application-config
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: ApplicationConfig
---
