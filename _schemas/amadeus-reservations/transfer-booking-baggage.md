---
description: Baggage schema
layout: schema
name: Baggage
properties_list:
- description: baggage capacity
  name: count
  type: integer
- description: baggage size code | name ------ | ---------------------------- S | Small M | Medium L | Large
  name: size
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-baggage-schema.json
slug: transfer-booking-baggage
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Baggage
---
