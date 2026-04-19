---
description: AirlineRemark schema
layout: schema
name: AirlineRemark
properties_list:
- description: ''
  name: subType
  type: object
- description: keyword code - only applicable for subType Keyword
  name: keyword
  type: string
- description: Code of the airline following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) When it apply to any airline, value is YY.
  name: airlineCode
  type: string
- description: remark free text
  name: text
  type: string
- description: Id of the concerned traveler
  name: travelerIds
  type: array
- description: Id of the concern flightOffers
  name: flightOfferIds
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-airline-remark-schema.json
slug: flight-order-management-airline-remark
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: AirlineRemark
---
