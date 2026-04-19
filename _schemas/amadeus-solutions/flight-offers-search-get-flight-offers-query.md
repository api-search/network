---
description: GetFlightOffersQuery schema
layout: schema
name: GetFlightOffersQuery
properties_list:
- description: The currency code, as defined in [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217), to reflect the currency in which this amount is expressed.
  name: currencyCode
  type: string
- description: 'Origins and Destinations must be properly ordered in time (chronological order in accordance with the timezone of each location) to describe the journey consistently. Dates and times must not be past '
  name: originDestinations
  type: array
- description: 'travelers in the trip. Maximum number of passengers older than 2 yo (CHILD, ADULT, YOUGHT): 9. Each adult can travel with one INFANT so maximum total number of passengers: 18'
  name: travelers
  type: array
- description: Allows enable one or more sources. If present in the list, these sources will be called by the system.
  name: sources
  type: array
- description: ''
  name: searchCriteria
  type: object
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-search-get-flight-offers-query-schema.json
slug: flight-offers-search-get-flight-offers-query
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: GetFlightOffersQuery
---
