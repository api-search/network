---
description: Price schema
layout: schema
name: Price
properties_list:
- description: ''
  name: currency
  type: string
- description: Total amount paid by the user
  name: total
  type: string
- description: Amount without taxes
  name: base
  type: string
- description: List of applicable fees
  name: fees
  type: array
- description: ''
  name: taxes
  type: array
- description: The amount of taxes which are refundable
  name: refundableTaxes
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-price-schema.json
slug: flight-create-orders-price
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Price
---
