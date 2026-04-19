---
description: Schema for a CVP Dialed Number Pattern (DNP). Dialed number patterns define how incoming calls are routed to specific VXML applications or call treatments based on the dialed number (DNIS). DNPs are a core configuration element in CVP that maps incoming numbers to call handling logic and integrates with ICM/UCCE routing.
layout: schema
name: Cisco Voice Portal Dialed Number Pattern
properties_list:
- description: Unique identifier for the pattern
  name: patternId
  type: string
- description: 'The dialed number pattern. Supports wildcards (* for any digits). Examples: 18005551234, 1800555*, *'
  name: pattern
  type: string
- description: Description of what this pattern routes to
  name: description
  type: string
- description: Call type determining how the call interacts with ICM/UCCE. Pre-route calls are sent to ICM before any treatment. Translation-route calls receive self-service treatment then route to ICM. Post-route c
  name: callType
  type: string
- description: VXML application associated with this pattern
  name: applicationName
  type: string
- description: Whether this pattern is active
  name: enabled
  type: boolean
- description: Pattern matching priority (lower number = higher priority)
  name: priority
  type: integer
- description: SIP server group for outbound routing
  name: sipServerGroup
  type: string
- description: Application to play while waiting for ICM route response
  name: ringtoneApplication
  type: string
- description: Application to play on error conditions
  name: errorApplication
  type: string
- description: Application to use in ICM survival mode (when ICM is unreachable)
  name: survivalApplication
  type: string
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-dialed-number-pattern.json
slug: cisco-voice-portal-dialed-number-pattern
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: Cisco Voice Portal Dialed Number Pattern
---
