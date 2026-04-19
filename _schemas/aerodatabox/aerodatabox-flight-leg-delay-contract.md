---
description: Delay statistics of a flight leg
layout: schema
name: FlightLegDelayContract
properties_list:
- description: Flight number
  name: number
  type: string
- description: Delay statistics of flight on departure at origins
  name: origins
  type: array
- description: Delay statistics of flight on arrival at destinations
  name: destinations
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-leg-delay-contract-schema.json
slug: aerodatabox-flight-leg-delay-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightLegDelayContract
---
