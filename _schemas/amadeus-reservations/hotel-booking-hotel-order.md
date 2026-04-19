---
description: An Hotel Order is one or several hotel bookings done for a set of guest.
layout: schema
name: HotelOrder
properties_list:
- description: Array of hotel-bookings
  name: hotelBookings
  type: array
- description: Reference and origin of the hotel order record
  name: associatedRecords
  type: array
- description: Self URL for retrieving the Hotel Order
  name: self
  type: string
- description: Resource name - Is set to "hotel-order"
  name: type
  type: string
- description: ''
  name: guests
  type: object
- description: Id of the hotelorder. It is a crucial information and must be stored in the client system as it is mandatory to provide it in any further step such as cancel or retrieve.
  name: id
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-hotel-order-schema.json
slug: hotel-booking-hotel-order
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: HotelOrder
---
