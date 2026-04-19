---
description: 'Positional information about flight: location, altitude, speed and track'
layout: schema
name: FlightLocationContract
properties_list:
- description: ''
  name: pressureAltitude
  type: object
- description: ''
  name: altitude
  type: object
- description: ''
  name: pressure
  type: object
- description: ''
  name: groundSpeed
  type: object
- description: ''
  name: trueTrack
  type: object
- description: Vertical speed, in feet per minute Not set if unknown or zero.
  name: vsiFpm
  type: integer
- description: Time (UTC) of when this positional data was reported
  name: reportedAtUtc
  type: string
- description: Latitude, in degrees
  name: lat
  type: number
- description: Longitude, in degrees
  name: lon
  type: number
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-location-contract-schema.json
slug: aerodatabox-flight-location-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightLocationContract
---
