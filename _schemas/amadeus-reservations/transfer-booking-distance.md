---
description: Distance schema
layout: schema
name: Distance
properties_list:
- description: 'great-circle distance between two locations. This distance thus do not take into account traffic conditions; international boundaries; mountains; water; or other elements that might make the a nearby '
  name: value
  type: integer
- description: unit of the distance
  name: unit
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-distance-schema.json
slug: transfer-booking-distance
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Distance
---
