---
class_count: 2
classes:
- Transfer
- TransferOrder
context_file: json-ld/amadeus-transfer-booking-transfer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/json-ld/amadeus-transfer-booking-transfer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Transfer Booking Transfer from Amadeus Reservations.
layout: jsonld
name: Amadeus Transfer Booking Transfer Context
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
  name: transferType
  type: string
- container: ''
  name: start
  type: string
- container: ''
  name: end
  type: string
- container: set
  name: stopOvers
  type: string
- container: set
  name: passenegerCharacteristics
  type: string
- container: ''
  name: duration
  type: string
- container: ''
  name: vehicle
  type: string
- container: ''
  name: serviceProvider
  type: string
- container: ''
  name: partnerInfo
  type: string
- container: ''
  name: quotation
  type: string
- container: ''
  name: converted
  type: string
- container: set
  name: extraServices
  type: string
- container: set
  name: equipment
  type: string
- container: set
  name: cancellationRules
  type: string
- container: set
  name: methodsOfPaymentAccepted
  type: string
- container: set
  name: discountCodes
  type: string
- container: ''
  name: distance
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: reference
  type: string
- container: set
  name: transfers
  type: string
- container: set
  name: passengers
  type: string
- container: ''
  name: agency
  type: string
property_count: 23
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
slug: amadeus-transfer-booking-transfer-context
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
