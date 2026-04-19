---
class_count: 6
classes:
- HotelProduct
- HotelProduct_PaymentPolicy
- HotelBooking
- HotelOrder
- HotelProduct_DepositPolicy
- description
context_file: json-ld/amadeus-hotel-booking-hotel-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-hotel-booking-hotel-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Booking Hotel from Amadeus Reservations.
layout: jsonld
name: Amadeus Hotel Booking Hotel Context
namespaces:
- prefix: amadeus
  uri: https://amadeus.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: checkInDate
  type: date
- container: ''
  name: checkOutDate
  type: date
- container: ''
  name: roomQuantity
  type: integer
- container: ''
  name: rateCode
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: commission
  type: reference
- container: ''
  name: room
  type: reference
- container: ''
  name: guests
  type: string
- container: ''
  name: price
  type: string
- container: ''
  name: policies
  type: reference
- container: ''
  name: rateFamilyEstimated
  type: reference
- container: set
  name: creditCards
  type: string
- container: set
  name: methods
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: bookingStatus
  type: string
- container: set
  name: roomAssociations
  type: string
- container: ''
  name: hotelOffer
  type: string
- container: ''
  name: hotel
  type: reference
- container: set
  name: hotelProviderInformation
  type: ''
- container: ''
  name: payment
  type: string
- container: ''
  name: travelAgentId
  type: string
- container: ''
  name: arrivalInformation
  type: reference
- container: set
  name: hotelBookings
  type: string
- container: set
  name: associatedRecords
  type: ''
- container: ''
  name: self
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: deadline
  type: dateTime
- container: ''
  name: acceptedPayments
  type: string
property_count: 29
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-hotel-booking-hotel-context
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
