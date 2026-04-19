---
description: Airport departure or arrival information
layout: schema
name: Airport
properties_list:
- description: IATA airport code
  name: airportCode
  type: string
- description: Full airport name
  name: airportName
  type: string
- description: Scheduled departure time with timezone
  name: scheduledDeparture
  type: string
- description: Estimated departure time with timezone
  name: estimatedDeparture
  type: string
- description: Scheduled arrival time with timezone
  name: scheduledArrival
  type: string
- description: Estimated arrival time with timezone
  name: estimatedArrival
  type: string
- description: Gate assignment
  name: gate
  type: string
- description: Terminal designation
  name: terminal
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-status-airport-schema.json
slug: alaska-air-flight-status-airport
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: Airport
---
