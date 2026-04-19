---
description: Facility schema
layout: schema
name: Facility
properties_list:
- description: Facility code, as described in the facility dictionary
  name: code
  type: string
- description: ''
  name: column
  type: string
- description: ''
  name: row
  type: string
- description: Position is either front, rear or seat (in case the facility takes the place of a seat)
  name: position
  type: string
- description: ''
  name: coordinates
  type: object
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/seat-map-display-facility-schema.json
slug: seat-map-display-facility
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: Facility
---
