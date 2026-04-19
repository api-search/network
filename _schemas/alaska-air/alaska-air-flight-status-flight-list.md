---
description: List of flights for a route and date
layout: schema
name: FlightList
properties_list:
- description: Array of flight summaries
  name: flights
  type: array
- description: Origin airport IATA code
  name: originAirport
  type: string
- description: Destination airport IATA code
  name: destinationAirport
  type: string
- description: Flight date
  name: flightDate
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-status-flight-list-schema.json
slug: alaska-air-flight-status-flight-list
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: FlightList
---
