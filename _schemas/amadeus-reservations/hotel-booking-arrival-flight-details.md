---
description: ArrivalFlightDetails schema
layout: schema
name: ArrivalFlightDetails
properties_list:
- description: Carrier code
  name: carrierCode
  type: string
- description: Flight segment number
  name: number
  type: string
- description: Departure or arrival information
  name: departure
  type: object
- description: Departure or arrival information
  name: arrival
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-arrival-flight-details-schema.json
slug: hotel-booking-arrival-flight-details
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: ArrivalFlightDetails
---
