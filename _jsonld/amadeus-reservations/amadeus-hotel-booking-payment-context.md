---
class_count: 2
classes:
- PaymentInput
- PaymentOutput
context_file: json-ld/amadeus-hotel-booking-payment-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-hotel-booking-payment-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Booking Payment from Amadeus Reservations.
layout: jsonld
name: Amadeus Hotel Booking Payment Context
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
  name: iataTravelAgency
  type: reference
- container: ''
  name: method
  type: string
- container: ''
  name: paymentCard
  type: reference
- container: ''
  name: billBack
  type: reference
- container: ''
  name: b2bWallet
  type: reference
property_count: 5
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-hotel-booking-payment-context
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
