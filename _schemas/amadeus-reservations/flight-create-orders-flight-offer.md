---
description: FlightOffer schema
layout: schema
name: FlightOffer
properties_list:
- description: the resource name
  name: type
  type: string
- description: Id of the flight offer
  name: id
  type: string
- description: ''
  name: source
  type: object
- description: If true, inform that a ticketing will be required at booking step.
  name: instantTicketingRequired
  type: boolean
- description: BOOK step ONLY - If true, allows to book a PNR without pricing. Only for the source "GDS"
  name: disablePricing
  type: boolean
- description: If true, upon completion of the booking, this pricing solution is expected to yield multiple records (a record contains booking information confirmed and stored, typically a Passenger Name Record (PNR
  name: nonHomogeneous
  type: boolean
- description: If true, the flight offer can be combined with other oneWays flight-offers to complete the whole journey (one-Way combinable feature).
  name: oneWay
  type: boolean
- description: If true, a payment card is mandatory to book this flight offer
  name: paymentCardRequired
  type: boolean
- description: If booked on the same day as the search (with respect to timezone), this flight offer is guaranteed to be thereafter valid for ticketing until this date (included). Unspecified when it does not make s
  name: lastTicketingDate
  type: string
- description: If booked on the same day as the search (with respect to timezone), this flight offer is guaranteed to be thereafter valid for ticketing until this date/time (included). Unspecified when it does not m
  name: lastTicketingDateTime
  type: string
- description: Number of seats bookable in a single request. Can not be higher than 9.
  name: numberOfBookableSeats
  type: number
- description: ''
  name: itineraries
  type: array
- description: ''
  name: price
  type: object
- description: ''
  name: pricingOptions
  type: object
- description: This option ensures that the system will only consider offers with these airlines as validating carrier.
  name: validatingAirlineCodes
  type: array
- description: Fare information for each traveler/segment
  name: travelerPricings
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-flight-offer-schema.json
slug: flight-create-orders-flight-offer
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: FlightOffer
---
