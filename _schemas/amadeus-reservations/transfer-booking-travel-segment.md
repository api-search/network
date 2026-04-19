---
description: A segment of an itinerary used by a traveler between 2 locations at a given date and time using a particular transportation type FLIGHT or TRAIN
layout: schema
name: TravelSegment
properties_list:
- description: ''
  name: transportationType
  type: object
- description: The flight number or train number, e.g. AF380
  name: transportationNumber
  type: string
- description: ''
  name: departure
  type: object
- description: ''
  name: arrival
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-travel-segment-schema.json
slug: transfer-booking-travel-segment
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: TravelSegment
---
