---
description: seat map information
layout: schema
name: SeatMap
properties_list:
- description: Ressource name
  name: type
  type: string
- description: item identifier
  name: id
  type: string
- description: ''
  name: self
  type: object
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
- description: providing the marketing airline carrier code
  name: carrierCode
  type: string
- description: the flight number as assigned by the marketing carrier
  name: number
  type: string
- description: ''
  name: operating
  type: object
- description: ''
  name: aircraft
  type: object
- description: reservation booking designator (RBD) of the carrier
  name: class
  type: string
- description: Id of the impacted flight offer
  name: flightOfferId
  type: string
- description: Id of the impacted segment
  name: segmentId
  type: string
- description: decks information
  name: decks
  type: array
- description: ''
  name: aircraftCabinAmenities
  type: object
- description: number of seats available for each passenger
  name: availableSeatsCounters
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/seat-map-display-seat-map-schema.json
slug: seat-map-display-seat-map
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: SeatMap
---
