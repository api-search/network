---
description: Address information
layout: schema
name: Address
properties_list:
- description: Line 1 = Street address, Line 2 = Apartment, suite, unit, building, floor, etc
  name: lines
  type: array
- description: 'Example: 74130'
  name: postalCode
  type: string
- description: ISO 3166-1 country code
  name: countryCode
  type: string
- description: 'Full city name. Example: Dublin'
  name: cityName
  type: string
- description: State code (two character standard IATA state code)
  name: stateCode
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-address-schema.json
slug: hotel-booking-address
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Address
---
