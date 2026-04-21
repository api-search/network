---
consumed_apis:
- hotel-booking
- flight-orders
- transfer-booking
description: Unified workflow capability for complete travel booking encompassing flight reservations, hotel bookings, and ground transfer arrangements. Used by online travel agencies, travel chatbots, and corporate travel management platforms to create end-to-end trip reservations.
layout: capability
name: Amadeus Travel Booking
operations:
- description: Create a confirmed flight booking.
  method: POST
  name: create-flight-order
  path: /v1/bookings/flights
- description: Retrieve a flight booking.
  method: GET
  name: get-flight-order
  path: /v1/bookings/flights/{orderId}
- description: Cancel a flight booking.
  method: DELETE
  name: cancel-flight-order
  path: /v1/bookings/flights/{orderId}
- description: Create a confirmed hotel booking.
  method: POST
  name: create-hotel-order
  path: /v1/bookings/hotels
- description: Create a confirmed transfer booking.
  method: POST
  name: create-transfer-order
  path: /v1/bookings/transfers
- description: Cancel a transfer booking.
  method: DELETE
  name: cancel-transfer-order
  path: /v1/bookings/transfers/{transferOrderId}
personas: []
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
search_terms:
- book a ground transfer (airport taxi, private car, or shuttle) for a traveler.
- create transfer order
- get flight order
- create hotel order
- create a confirmed airline reservation from a priced flight offer.
- create flight booking
- create flight order
- hotel reservation operations.
- individual flight order management.
- hotel reservation creation.
- cancel a flight booking.
- cancel flight order
- flight reservation operations.
- create a confirmed flight booking.
- amadeus
- airline reservation creation and management.
- cancel a transfer booking.
- create hotel booking
- cancel an existing confirmed ground transfer reservation.
- ground transfer reservation operations.
- travel
- transfers
- flights
- reservations
- developer building ai-powered travel assistants that create bookings conversationally.
- Travel Chatbot Developer
- individual transfer management.
- create a confirmed hotel booking.
- end-to-end travel booking combining flights, hotels, and transfers.
- cancel transfer order
- ground transportation booking and management.
- create a confirmed hotel reservation from a hotel offer at any of 150,000+ hotels worldwide.
- create transfer booking
- retrieve a flight booking.
- cancel an existing confirmed flight reservation.
- hotels
- booking
- Travel Booking Agent
- retrieve details of an existing flight reservation by order id.
- get flight booking
- cancel transfer booking
- cancel flight booking
- human or automated agent creating and managing travel reservations on behalf of travelers.
- create a confirmed transfer booking.
slug: travel-booking
tags:
- Amadeus
- Booking
- Flights
- Hotels
- Transfers
- Travel
tools:
- description: Create a confirmed airline reservation from a priced flight offer.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-flight-booking
- description: Retrieve details of an existing flight reservation by order ID.
  hints:
    openWorld: true
    readOnly: true
  name: get-flight-booking
- description: Cancel an existing confirmed flight reservation.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: cancel-flight-booking
- description: Create a confirmed hotel reservation from a hotel offer at any of 150,000+ hotels worldwide.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-hotel-booking
- description: Book a ground transfer (airport taxi, private car, or shuttle) for a traveler.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-transfer-booking
- description: Cancel an existing confirmed ground transfer reservation.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: cancel-transfer-booking
---
