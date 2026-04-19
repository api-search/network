---
description: defining a flight segment; including both operating and marketing details when applicable
layout: schema
name: FlightSegment
properties_list:
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
- description: providing the airline / carrier code
  name: carrierCode
  type: string
- description: the flight number as assigned by the carrier
  name: number
  type: string
- description: ''
  name: aircraft
  type: object
- description: ''
  name: operating
  type: object
- description: stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
  name: duration
  type: string
- description: information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge...
  name: stops
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/branded-fares-upsell-flight-segment-schema.json
slug: branded-fares-upsell-flight-segment
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: FlightSegment
---
