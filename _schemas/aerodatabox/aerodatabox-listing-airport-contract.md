---
description: Flight's airport reference contract
layout: schema
name: ListingAirportContract
properties_list:
- description: ICAO code of the airport
  name: icao
  type: string
- description: IATA code of the airport
  name: iata
  type: string
- description: Code of the airport within the local or national codification system
  name: localCode
  type: string
- description: Name of the airport
  name: name
  type: string
- description: Shortened name of the airport
  name: shortName
  type: string
- description: Name of the municipality this airport belongs to
  name: municipalityName
  type: string
- description: ''
  name: location
  type: object
- description: Two-letter country code of the airport
  name: countryCode
  type: string
- description: Time zone of the airport in Olson format (e.g. "Europe/Amsterdam")
  name: timeZone
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-listing-airport-contract-schema.json
slug: aerodatabox-listing-airport-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: ListingAirportContract
---
