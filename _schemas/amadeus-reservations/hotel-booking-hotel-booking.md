---
description: An hotel booking represent one or several rooms booked in the same physical hotel. There is always a reference to this booking, provided by the hotel provider, stored in associated records section.
layout: schema
name: HotelBooking
properties_list:
- description: Type of data - set to "hotel-booking".
  name: type
  type: string
- description: Unique ID of the hotel booking ID. It is computed by Amadeus System based on technical data.
  name: id
  type: string
- description: 'Status of the booking - Possible values - "CONFIRMED" - "PENDING" for on-request - "CANCELLED" (It will be returned only in the retrieve byHistory as it repreents a DELETED resource.) - "On HOLD" for '
  name: bookingStatus
  type: string
- description: Array of room associations. Each room association correlates one single room to guest(s), a payment and an hotel offer. If multiple identical rooms are requested, one roomAssociation is created per ho
  name: roomAssociations
  type: array
- description: ''
  name: hotelOffer
  type: object
- description: Hotel Content
  name: hotel
  type: object
- description: References and origin of the hotel bookings records
  name: hotelProviderInformation
  type: array
- description: ''
  name: payment
  type: object
- description: Travel Agent ID also called Booking source or IATA number. - When received in booking request, it indicates that the travel agent wants to override the booking source receiving the commission. - If no
  name: travelAgentId
  type: string
- description: Optional information on the way the guest is arriving to the hotel. Today the application only supports Flight details. If this information is provided at booking creation time, it is displayed in the
  name: arrivalInformation
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/hotel-booking-hotel-booking-schema.json
slug: hotel-booking-hotel-booking
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: HotelBooking
---
