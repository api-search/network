---
description: Contract containing information on distance and approximate flight time between specified airports
layout: schema
name: AirportDistanceTimeContract
properties_list:
- description: ''
  name: from
  type: object
- description: ''
  name: to
  type: object
- description: ''
  name: greatCircleDistance
  type: object
- description: Approximate flight time based on re-calculation of great circle distance against statistical duration average of multiple flights covered similar distance before.
  name: approxFlightTime
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-airport-distance-time-contract-schema.json
slug: aerodatabox-airport-distance-time-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: AirportDistanceTimeContract
---
