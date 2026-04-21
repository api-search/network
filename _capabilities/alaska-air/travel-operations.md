---
consumed_apis:
- alaska-flight-status
- alaska-cargo
description: Workflow capability combining Alaska Airlines Flight Status and Cargo APIs for travel operations management. Enables travel agents, corporate travel managers, and freight forwarders to track flights, monitor cargo shipments, and get rate estimates in a unified interface.
layout: capability
name: Alaska Airlines Travel Operations
operations:
- description: List Alaska Airlines flights by route and date
  method: GET
  name: list-flights
  path: /v1/flights
- description: Get real-time status for a specific flight
  method: GET
  name: get-flight-status
  path: /v1/flights/{flightNumber}/status
- description: List cargo shipments
  method: GET
  name: list-cargo-shipments
  path: /v1/cargo/shipments
- description: Book a new cargo shipment
  method: POST
  name: book-cargo-shipment
  path: /v1/cargo/shipments
- description: Track cargo shipment by AWB number
  method: GET
  name: track-cargo-shipment
  path: /v1/cargo/shipments/{awbNumber}
- description: Get cargo rate estimate
  method: POST
  name: get-cargo-rate
  path: /v1/cargo/rates
personas: []
provider_name: Alaska Airlines
provider_slug: alaska-air
search_terms:
- Travel Agent
- get alaska flight status
- aviation
- loyalty
- travel operations
- mileage plan member management and partner miles
- list alaska flights
- track cargo shipment
- get real-time status for a specific alaska airlines flight including departure/arrival times, gate, and delay information.
- list alaska airlines flights for a specific route and date with real-time status, delays, and gate assignments.
- flight status
- track alaska air cargo shipment by air waybill number with event history
- cargo shipment booking and listing
- cargo booking, tracking, and rate management
- real-time flight status
- alaska airlines
- track cargo shipment by awb number
- list flights
- cargo shipment tracking
- Freight Forwarder
- get flight status
- get rate estimate for alaska air cargo shipment based on origin, destination, weight, and number of pieces.
- book a new cargo shipment
- list alaska airlines flights by route and date
- book a new alaska air cargo shipment to 115+ destinations worldwide
- travel
- cargo
- flight tracking and cargo management for travel operations
- real-time flight status, schedules, and airport data
- cargo rate estimation
- travel professional monitoring alaska airlines flight status and delays for customer itinerary management.
- book cargo shipment
- cargo professional booking and tracking alaska air cargo shipments across 115+ domestic and international destinations.
- get real-time status for a specific flight
- flight status and scheduling
- get cargo rate estimate
- airlines
- get cargo rate
- Corporate Travel Manager
- list cargo shipments
- corporate travel manager tracking employee flights on alaska airlines and managing cargo logistics.
slug: travel-operations
tags:
- Alaska Airlines
- Travel Operations
- Aviation
- Cargo
- Flight Status
tools:
- description: List Alaska Airlines flights for a specific route and date with real-time status, delays, and gate assignments.
  hints:
    openWorld: false
    readOnly: true
  name: list-alaska-flights
- description: Get real-time status for a specific Alaska Airlines flight including departure/arrival times, gate, and delay information.
  hints:
    openWorld: false
    readOnly: true
  name: get-alaska-flight-status
- description: Get rate estimate for Alaska Air Cargo shipment based on origin, destination, weight, and number of pieces.
  hints:
    openWorld: false
    readOnly: true
  name: get-cargo-rate-estimate
- description: Book a new Alaska Air Cargo shipment to 115+ destinations worldwide
  hints:
    openWorld: false
    readOnly: false
  name: book-cargo-shipment
- description: Track Alaska Air Cargo shipment by Air Waybill number with event history
  hints:
    openWorld: false
    readOnly: true
  name: track-cargo-shipment
---
