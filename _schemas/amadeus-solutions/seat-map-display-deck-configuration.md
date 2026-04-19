---
description: deck dimensions are used as a reference to display the entire aircraft or to the section associated to the requested cabin (or set of cabins)
layout: schema
name: DeckConfiguration
properties_list:
- description: Width (y-axis) of the deck.
  name: width
  type: integer
- description: Length (x-axis) of the deck.
  name: length
  type: integer
- description: seat row where the deck is starting
  name: startSeatRow
  type: integer
- description: seat row where the deck is ending
  name: endSeatRow
  type: integer
- description: Start x coordinate of the wings.The wings display starts relatively to the length.
  name: startWingsX
  type: integer
- description: End x coordinate of the wings.The wings display ends relatively to the length.
  name: endWingsX
  type: integer
- description: seat row where the wing is starting
  name: startWingsRow
  type: integer
- description: seat row where the wing is ending
  name: endWingsRow
  type: integer
- description: X coordinate of the exit rows.The exit rows are displayed relatively to the length.
  name: exitRowsX
  type: array
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/seat-map-display-deck-configuration-schema.json
slug: seat-map-display-deck-configuration
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: DeckConfiguration
---
