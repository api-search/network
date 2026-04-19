---
description: ''
layout: schema
name: RealtimeStatistics
properties_list:
- description: ''
  name: timestamp
  type: string
- description: Current number of active calls
  name: activeCalls
  type: integer
- description: ''
  name: callsInProgress
  type: object
- description: Current calls per second rate
  name: callsPerSecond
  type: number
- description: Peak active calls in current period
  name: peakActiveCalls
  type: integer
- description: ''
  name: serverMetrics
  type: array
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-reporting-realtime-statistics-schema.json
slug: cisco-voice-portal-reporting-realtime-statistics
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: RealtimeStatistics
---
