---
description: Flight plan contract
layout: schema
name: FlightPlanContract
properties_list:
- description: ''
  name: flightRules
  type: object
- description: ''
  name: flightType
  type: object
- description: No. of revision of the flight plan
  name: revisionNo
  type: integer
- description: ''
  name: status
  type: object
- description: Route information for the flight as filed in the flight plan
  name: route
  type: string
- description: ''
  name: altitude
  type: object
- description: ''
  name: airspeed
  type: object
- description: Time (UTC) of the latest known update to the flight plan
  name: lastUpdatedUtc
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-plan-contract-schema.json
slug: aerodatabox-flight-plan-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightPlanContract
---
