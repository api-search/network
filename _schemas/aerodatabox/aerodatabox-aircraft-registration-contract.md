---
description: Aircraft registration data
layout: schema
name: AircraftRegistrationContract
properties_list:
- description: Tail-number of the aircraft
  name: reg
  type: string
- description: Indicator if aircraft is operational under this registration
  name: active
  type: boolean
- description: ICAO 24 bit Mode-S hexadecimal transponder address
  name: hexIcao
  type: string
- description: Name of the airline operating the aircraft
  name: airlineName
  type: string
- description: Date of assigning current registration
  name: registrationDate
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-aircraft-registration-contract-schema.json
slug: aerodatabox-aircraft-registration-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AircraftRegistrationContract
---
