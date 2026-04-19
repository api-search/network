---
description: Specific type to convey a list of string for specific information type ( via qualifier) in specific character set, or language
layout: schema
name: QualifiedFreeText
properties_list:
- description: Free Text
  name: text
  type: string
- description: see RFC 5646
  name: lang
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-qualified-free-text-schema.json
slug: hotel-booking-qualified-free-text
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: QualifiedFreeText
---
