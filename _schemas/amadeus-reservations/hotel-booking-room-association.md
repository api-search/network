---
description: Room Association represents a room booked in an hotel, the guests sleeping in this room, the hotel loyalty program if any, plus special request if any.
layout: schema
name: roomAssociation
properties_list:
- description: Array of guest references listing all the guests occupying the room. For each guest, the reference provided is the id also provided in guest section, except at booking creation time (in this only case
  name: guestReferences
  type: array
- description: special request to send to the reception (optional)
  name: specialRequest
  type: string
- description: Hotel offerID received in availability response, identifying the product to book.
  name: hotelOfferId
  type: string
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-room-association-schema.json
slug: hotel-booking-room-association
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: roomAssociation
---
