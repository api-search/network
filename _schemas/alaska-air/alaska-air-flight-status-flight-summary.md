---
description: Summary flight information for route listing
layout: schema
name: FlightSummary
properties_list:
- description: Flight number
  name: flightNumber
  type: string
- description: Operating carrier code
  name: carrier
  type: string
- description: Flight status
  name: status
  type: string
- description: Scheduled departure time
  name: scheduledDeparture
  type: string
- description: Scheduled arrival time
  name: scheduledArrival
  type: string
- description: Delay in minutes
  name: delayMinutes
  type: integer
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-status-flight-summary-schema.json
slug: alaska-air-flight-status-flight-summary
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: FlightSummary
---
