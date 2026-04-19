---
description: ''
layout: schema
name: CallFlowElement
properties_list:
- description: Name of the call flow element
  name: elementName
  type: string
- description: Type of element. Voice elements interact with the caller, action elements perform backend operations, decision elements control flow logic, and subdialog elements invoke sub-applications.
  name: elementType
  type: string
- description: ''
  name: description
  type: string
- description: Java class implementing the element
  name: className
  type: string
- description: Element-specific configuration
  name: configParameters
  type: object
- description: Element exit paths and their targets
  name: exits
  type: array
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-vxml-services-call-flow-element-schema.json
slug: cisco-voice-portal-vxml-services-call-flow-element
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: CallFlowElement
---
