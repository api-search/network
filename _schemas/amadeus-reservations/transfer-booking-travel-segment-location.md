---
description: The flight or train departure/arrival date&time, location information
layout: schema
name: TravelSegmentLocation
properties_list:
- description: The railway UIC code defined by the worldwide railway organization, e.g. 7400001
  name: uicCode
  type: string
- description: The airport code from IATA table codes, e.g. CDG
  name: iataCode
  type: string
- description: The date and time inspired from ISO 8601 (YYYY-MM-DDTHH:MM:SS) format
  name: localDateTime
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-travel-segment-location-schema.json
slug: transfer-booking-travel-segment-location
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: TravelSegmentLocation
---
