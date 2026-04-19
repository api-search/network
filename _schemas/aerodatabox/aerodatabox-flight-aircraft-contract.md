---
description: Flight's aircraft reference contract
layout: schema
name: FlightAircraftContract
properties_list:
- description: Tail-number of the aircraft
  name: reg
  type: string
- description: ICAO 24 bit Mode-S hexadecimal transponder address
  name: modeS
  type: string
- description: Aircraft name and model
  name: model
  type: string
- description: ''
  name: image
  type: object
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-aircraft-contract-schema.json
slug: aerodatabox-flight-aircraft-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightAircraftContract
---
