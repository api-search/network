---
description: Schema for a CVP VXML application. Applications are VoiceXML programs typically built with Cisco Unified Call Studio that execute on the CVP VXML Server to provide interactive voice response (IVR) functionality. Applications consist of call flow elements including voice elements, action elements, and decision elements.
layout: schema
name: Cisco Voice Portal Application
properties_list:
- description: Unique identifier for the application
  name: applicationId
  type: string
- description: Name of the application as deployed
  name: applicationName
  type: string
- description: Type of VXML application. Call Studio applications are built with Cisco Unified Call Studio. Standalone VXML applications are hand-coded VoiceXML. Micro-applications are built-in CVP IVR functions.
  name: applicationType
  type: string
- description: Current deployment and operational status
  name: status
  type: string
- description: Application version
  name: version
  type: string
- description: Description of the application purpose
  name: description
  type: string
- description: Name of the starting call flow element
  name: entryPoint
  type: string
- description: Call flow elements that make up the application
  name: elements
  type: array
- description: Application-level runtime configuration parameters
  name: configParameters
  type: object
- description: Default language for prompts and ASR
  name: defaultLanguage
  type: string
- description: Allowed caller input modes
  name: inputModes
  type: array
- description: VXML Servers this application is deployed to
  name: deployedServers
  type: array
- description: Path to associated audio prompt files
  name: mediaDirectory
  type: string
- description: Path to associated speech grammar files
  name: grammarDirectory
  type: string
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-application.json
slug: cisco-voice-portal-application
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: Cisco Voice Portal Application
---
