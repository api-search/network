---
class_count: 2
classes:
- Vehicle
- description
context_file: json-ld/amadeus-transfer-booking-vehicle-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-transfer-booking-vehicle-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Transfer Booking Vehicle from Amadeus Reservations.
layout: jsonld
name: Amadeus Transfer Booking Vehicle Context
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
  name: code
  type: string
- container: ''
  name: category
  type: string
- container: set
  name: seats
  type: string
- container: set
  name: baggages
  type: string
- container: ''
  name: imageURL
  type: string
property_count: 5
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-transfer-booking-vehicle-context
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
