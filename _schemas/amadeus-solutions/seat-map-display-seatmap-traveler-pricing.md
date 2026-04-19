---
description: SeatmapTravelerPricing schema
layout: schema
name: SeatmapTravelerPricing
properties_list:
- description: Traveler id
  name: travelerId
  type: string
- description: Seat availability for this specific traveler. Allows better seat choice per traveler
  name: seatAvailabilityStatus
  type: string
- description: Price for a given seat
  name: price
  type: object
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/seat-map-display-seatmap-traveler-pricing-schema.json
slug: seat-map-display-seatmap-traveler-pricing
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: SeatmapTravelerPricing
---
