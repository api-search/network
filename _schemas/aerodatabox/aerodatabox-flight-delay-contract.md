---
description: Delay statistics for a flight movement
layout: schema
name: FlightDelayContract
properties_list:
- description: ICAO code of the airport at which statistics is observed
  name: airportIcao
  type: string
- description: ''
  name: class
  type: object
- description: Hour on which flight is scheduled (represented in UTC). If provided, it separates the statistics for the same flight departing/arriving at different time of day on different days within the observed p
  name: scheduledHourUtc
  type: integer
- description: 'Median historic delay of the flight (format: [-]hh:mm:ss). Value can be negative (therefore, means early occurence).'
  name: medianDelay
  type: string
- description: Distribution of historic delays of the flight in percentiles from 5 percentile to 95 percentile in steps of 5 percentile, allowing for a more detailed analysis of delay patterns beyond simple averages
  name: delayPercentiles
  type: array
- description: The number of flight movements taken into account to calculate this statistics.
  name: numConsideredFlights
  type: integer
- description: Brackets containing information more detailed information about how many flights were delayed/early per specific delay range brackets (e.g. late from 15 to 30 minutes, from 30 to 60, etc.)
  name: numFlightsDelayedBrackets
  type: array
- description: The beginning of the time range within which flght delay information is calculated (represented in UTC time)
  name: fromUtc
  type: string
- description: The end of the time range within which flght delay information is calculated (represented in UTC time)
  name: toUtc
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-flight-delay-contract-schema.json
slug: aerodatabox-flight-delay-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: FlightDelayContract
---
