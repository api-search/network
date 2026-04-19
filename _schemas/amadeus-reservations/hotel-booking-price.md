---
description: Price valuation information
layout: schema
name: Price
properties_list:
- description: currency Code apply to all elements of the price
  name: currency
  type: string
- description: sellingTotal = Total + margins + markup + totalFees - discounts
  name: sellingTotal
  type: string
- description: total = base + totalTaxes
  name: total
  type: string
- description: ''
  name: base
  type: string
- description: ''
  name: markups
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-price-schema.json
slug: hotel-booking-price
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Price
---
