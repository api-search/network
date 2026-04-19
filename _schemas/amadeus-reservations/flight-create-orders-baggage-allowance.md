---
description: baggageAllowance
layout: schema
name: BaggageAllowance
properties_list:
- description: Total number of units
  name: quantity
  type: integer
- description: Weight of the baggage allowance
  name: weight
  type: integer
- description: Code to qualify unit as pounds or kilos
  name: weightUnit
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-create-orders-baggage-allowance-schema.json
slug: flight-create-orders-baggage-allowance
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: BaggageAllowance
---
