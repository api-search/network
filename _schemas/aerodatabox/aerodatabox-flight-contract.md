---
description: Individiual flight contract
layout: schema
name: FlightContract
properties_list:
- description: ''
  name: greatCircleDistance
  type: object
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
- description: ''
  name: flightPlan
  type: object
- description: Time (UTC) of the latest update of flight information (excluding Location)
  name: lastUpdatedUtc
  type: string
- description: Flight Number
  name: number
  type: string
- description: ATC call-sign of the flight
  name: callSign
  type: string
- description: ''
  name: status
  type: object
- description: ''
  name: codeshareStatus
  type: object
- description: Is cargo flight
  name: isCargo
  type: boolean
- description: ''
  name: aircraft
  type: object
- description: ''
  name: airline
  type: object
- description: ''
  name: location
  type: object
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-contract-schema.json
slug: aerodatabox-flight-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightContract
---
