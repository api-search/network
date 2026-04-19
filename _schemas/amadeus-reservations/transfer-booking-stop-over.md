---
description: Location of the stop over or the several stop over points. It can be defined either using IATA code or Address (address line, zip, country, city, state, latitude, longitude). Vehicle change via stop overs is not supported.
layout: schema
name: StopOver
properties_list:
- description: transfer stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M.
  name: duration
  type: string
- description: sequence number of the stop e.g. 3
  name: sequenceNumber
  type: number
- description: ''
  name: location
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-stop-over-schema.json
slug: transfer-booking-stop-over
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: StopOver
---
