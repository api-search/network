---
description: Single airport data
layout: schema
name: AirportContract
properties_list:
- description: ICAO code of the airport
  name: icao
  type: string
- description: IATA code of the airport
  name: iata
  type: string
- description: Code of the airport within the local or national coding system
  name: localCode
  type: string
- description: Shortened name of the airport
  name: shortName
  type: string
- description: Full name of the airport (derived from own airport name and municipality name)
  name: fullName
  type: string
- description: Name of the municipality this airport belongs to
  name: municipalityName
  type: string
- description: ''
  name: location
  type: object
- description: ''
  name: elevation
  type: object
- description: ''
  name: country
  type: object
- description: ''
  name: continent
  type: object
- description: Time zone of the airport in Olson format (e.g. "Europe/Amsterdam")
  name: timeZone
  type: string
- description: ''
  name: urls
  type: object
- description: List of runway information, if requested
  name: runways
  type: array
- description: ''
  name: currentTime
  type: object
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-airport-contract-schema.json
slug: aerodatabox-airport-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AirportContract
---
