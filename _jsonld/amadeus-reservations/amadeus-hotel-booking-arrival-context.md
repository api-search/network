---
class_count: 1
classes:
- ArrivalFlightDetails
context_file: json-ld/amadeus-hotel-booking-arrival-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-hotel-booking-arrival-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Booking Arrival from Amadeus Reservations.
layout: jsonld
name: Amadeus Hotel Booking Arrival Context
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
  name: carrierCode
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: departure
  type: reference
- container: ''
  name: arrival
  type: reference
property_count: 4
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-hotel-booking-arrival-context
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
