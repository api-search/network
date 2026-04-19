---
description: Flight arrival or departure information
layout: schema
name: FlightAirportMovementContract
properties_list:
- description: ''
  name: airport
  type: object
- description: ''
  name: scheduledTime
  type: object
- description: ''
  name: revisedTime
  type: object
- description: ''
  name: predictedTime
  type: object
- description: ''
  name: runwayTime
  type: object
- description: Terminal of the flight
  name: terminal
  type: string
- description: Check-in desk(s) for the flight (only for departing flights)
  name: checkInDesk
  type: string
- description: Gate of (un)boarding for the flight
  name: gate
  type: string
- description: Baggage belt(s) for the flight (only for arriving flights)
  name: baggageBelt
  type: string
- description: Name of a runway of landing (for arriving flights) or take-off (for departing flights), if known.
  name: runway
  type: string
- description: Array of quality characteristics of the data. Check this to know which information you can expect within this contract (basic, live and/or approximate data).
  name: quality
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-airport-movement-contract-schema.json
slug: aerodatabox-flight-airport-movement-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightAirportMovementContract
---
