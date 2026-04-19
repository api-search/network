---
class_count: 1
classes:
- CreateHotelBooking
context_file: json-ld/amadeus-hotel-booking-create-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-hotel-booking-create-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Booking Create from Amadeus Reservations.
layout: jsonld
name: Amadeus Hotel Booking Create Context
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
  name: arrivalInformation
  type: reference
- container: ''
  name: payment
  type: string
- container: set
  name: roomAssociations
  type: string
- container: ''
  name: travelAgent
  type: reference
property_count: 4
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-hotel-booking-create-context
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
