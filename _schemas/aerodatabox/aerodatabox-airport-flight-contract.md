---
description: Flight data contract represented in airport schedule
layout: schema
name: AirportFlightContract
properties_list:
- description: ''
  name: movement
  type: object
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
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
schema_file: json-schema/aerodatabox-airport-flight-contract-schema.json
slug: aerodatabox-airport-flight-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AirportFlightContract
---
