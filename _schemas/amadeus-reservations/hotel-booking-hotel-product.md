---
description: Hotel Offer
layout: schema
name: HotelProduct
properties_list:
- description: check-in date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is today date (no dates in the past).
  name: checkInDate
  type: string
- description: check-out date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is `checkInDate`+1.
  name: checkOutDate
  type: string
- description: number of rooms (1-9)
  name: roomQuantity
  type: integer
- description: Special Rate - Provider Response Code (3 chars) Examples * RAC - Rack * BAR - Best Available Rate * PRO - Promotional * COR - Corporate * GOV - Government (qualified) * AAA - AAA (qualified) * BNB - B
  name: rateCode
  type: string
- description: 'Special Rate Category Examples: ASSOCIATION FAMILY_PLAN'
  name: category
  type: string
- description: ''
  name: commission
  type: object
- description: ''
  name: room
  type: object
- description: ''
  name: guests
  type: object
- description: price information
  name: price
  type: object
- description: Booking Rules
  name: policies
  type: object
- description: The estimated rate code family of the offer. Grouping various rate plan codes that belongs to the same family and indicates the type of the rate
  name: rateFamilyEstimated
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-hotel-product-schema.json
slug: hotel-booking-hotel-product
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: HotelProduct
---
