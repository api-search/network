---
class_count: 1
classes:
- guests
context_file: json-ld/amadeus-hotel-booking-guests-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-hotel-booking-guests-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Booking Guests from Amadeus Reservations.
layout: jsonld
name: Amadeus Hotel Booking Guests Context
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
  name: adults
  type: integer
- container: set
  name: childAges
  type: integer
property_count: 2
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-hotel-booking-guests-context
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
