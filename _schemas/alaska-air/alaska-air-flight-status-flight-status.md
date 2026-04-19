---
description: Real-time status for an Alaska Airlines flight
layout: schema
name: FlightStatus
properties_list:
- description: Flight number including carrier code
  name: flightNumber
  type: string
- description: Flight operating date
  name: flightDate
  type: string
- description: Operating carrier code
  name: carrier
  type: string
- description: Flight status description
  name: status
  type: string
- description: Delay in minutes (0 if on time)
  name: delayMinutes
  type: integer
- description: Reason for delay if applicable
  name: delayReason
  type: string
- description: ''
  name: origin
  type: object
- description: ''
  name: destination
  type: object
- description: ''
  name: aircraft
  type: object
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-status-flight-status-schema.json
slug: alaska-air-flight-status-flight-status
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: FlightStatus
---
