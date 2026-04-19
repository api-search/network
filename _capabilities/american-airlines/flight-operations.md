---
consumed_apis:
- aa-runway
description: Unified workflow for travel applications and agents accessing American Airlines flight data, status, and booking capabilities. Serves travel technology teams and booking platform developers.
layout: capability
name: American Airlines Flight Operations
operations:
- description: Search flight schedules
  method: GET
  name: search-flights
  path: /v1/flights
- description: Get flight status
  method: GET
  name: get-flight-status
  path: /v1/flights/{flightId}/status
personas: []
provider_name: American Airlines
provider_slug: american-airlines
search_terms:
- travel
- flight search and schedules
- travel technology
- travel app workflow for searching and tracking american airlines flights
- search american airlines flight schedules by origin, destination, and date
- flights
- get flight status
- real-time flight status
- search flights
- developer experience
- search flight schedules
- aviation
- Travel Technology Developer
- uses flight data to assist customers with bookings
- booking
- airlines
- american airlines
- get real-time status of an american airlines flight
- builds travel apps integrating american airlines flight data
- flight operations
- Booking Agent
slug: flight-operations
tags:
- American Airlines
- Airlines
- Flight Operations
- Travel Technology
- Booking
tools:
- description: Search American Airlines flight schedules by origin, destination, and date
  hints:
    openWorld: true
    readOnly: true
  name: search-flights
- description: Get real-time status of an American Airlines flight
  hints:
    readOnly: true
  name: get-flight-status
---
