---
description: This model allows the creation of an hotel order.
layout: schema
name: CreateHotelBooking
properties_list:
- description: Optional information on the way the guest is arriving to the hotel. Today the application only supports Flight details.
  name: arrivalInformation
  type: object
- description: ''
  name: payment
  type: object
- description: Is to correlate a room to a guest and an offer.
  name: roomAssociations
  type: array
- description: Travel Agent details
  name: travelAgent
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-create-hotel-booking-schema.json
slug: hotel-booking-create-hotel-booking
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: CreateHotelBooking
---
