---
description: Co2Emission schema
layout: schema
name: Co2Emission
properties_list:
- description: Weight of Co2 emitted for the concerned segment
  name: weight
  type: integer
- description: Code to qualify unit as pounds or kilos
  name: weightUnit
  type: string
- description: ''
  name: cabin
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/flight-order-management-co2-emission-schema.json
slug: flight-order-management-co2-emission
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Co2Emission
---
