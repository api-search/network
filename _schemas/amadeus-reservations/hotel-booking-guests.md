---
description: guests schema
layout: schema
name: guests
properties_list:
- description: number of adult guests (1-9) per room
  name: adults
  type: integer
- description: Comma separated list of ages of each child at the time of check-out from the hotel. If several children have the same age, the ages will be repeated.
  name: childAges
  type: array
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-guests-schema.json
slug: hotel-booking-guests
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: guests
---
