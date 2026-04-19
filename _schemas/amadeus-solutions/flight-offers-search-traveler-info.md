---
description: TravelerInfo schema
layout: schema
name: TravelerInfo
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: travelerType
  type: object
- description: if type="HELD_INFANT", corresponds to the adult travelers's id who will share the seat
  name: associatedAdultId
  type: string
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/flight-offers-search-traveler-info-schema.json
slug: flight-offers-search-traveler-info
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: TravelerInfo
---
