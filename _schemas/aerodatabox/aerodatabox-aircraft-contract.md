---
description: Single aircraft data
layout: schema
name: AircraftContract
properties_list:
- description: Unique ID of the aircraft record in our database
  name: id
  type: integer
- description: Tail-number of the aircraft
  name: reg
  type: string
- description: Indicator if aircraft is operational under this registration
  name: active
  type: boolean
- description: Serial number
  name: serial
  type: string
- description: ICAO 24 bit Mode-S hexadecimal transponder address
  name: hexIcao
  type: string
- description: Name of the airline operating the aircraft
  name: airlineName
  type: string
- description: IATA-type of the aircraft
  name: iataType
  type: string
- description: Short variant of IATA-code of the aircraft
  name: iataCodeShort
  type: string
- description: ICAO-code of the aircraft
  name: icaoCode
  type: string
- description: Model of the aircraft
  name: model
  type: string
- description: Model code of the aircraft
  name: modelCode
  type: string
- description: Number of passenger seats
  name: numSeats
  type: integer
- description: Date of roll-out (UTC)
  name: rolloutDate
  type: string
- description: First flight date
  name: firstFlightDate
  type: string
- description: Date of delivery to the owner
  name: deliveryDate
  type: string
- description: Date of assigning current registration
  name: registrationDate
  type: string
- description: Type name
  name: typeName
  type: string
- description: Number of engines
  name: numEngines
  type: integer
- description: ''
  name: engineType
  type: object
- description: Marker if aircraft is cargo or not
  name: isFreighter
  type: boolean
- description: Production line
  name: productionLine
  type: string
- description: Age of the aircraft in year
  name: ageYears
  type: number
- description: ''
  name: verified
  type: boolean
- description: ''
  name: image
  type: object
- description: An aircraft may have a history of past registrations with other airlines or operators. This field represents a total number of registration records known in our database.
  name: numRegistrations
  type: integer
- description: A history of all registrations with other airlines or operators (if provided by the endpoint).
  name: registrations
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-aircraft-contract-schema.json
slug: aerodatabox-aircraft-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AircraftContract
---
