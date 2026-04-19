---
description: ''
layout: schema
name: RoutingResult
properties_list:
- description: ''
  name: dialedNumber
  type: string
- description: Whether a matching pattern was found
  name: matched
  type: boolean
- description: The dialed number pattern that matched
  name: matchedPattern
  type: string
- description: ''
  name: callType
  type: string
- description: Application that would handle the call
  name: applicationName
  type: string
- description: Resulting route destination
  name: routeDestination
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-call-control-routing-result-schema.json
slug: cisco-voice-portal-call-control-routing-result
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: RoutingResult
---
