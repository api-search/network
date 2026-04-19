---
description: Transfer schema
layout: schema
name: Transfer
properties_list:
- description: amadeus transfer service type value | description -------------- | ------------------------ PRIVATE | Private transfer from point to point SHARED | Shared transfer from point to point TAXI | Taxi rese
  name: transferType
  type: string
- description: ''
  name: start
  type: object
- description: ''
  name: end
  type: object
- description: ''
  name: stopOvers
  type: array
- description: ''
  name: passenegerCharacteristics
  type: array
- description: transfer duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
  name: duration
  type: string
- description: ''
  name: vehicle
  type: object
- description: ''
  name: serviceProvider
  type: object
- description: ''
  name: partnerInfo
  type: object
- description: ''
  name: quotation
  type: object
- description: ''
  name: converted
  type: object
- description: ''
  name: extraServices
  type: array
- description: ''
  name: equipment
  type: array
- description: ''
  name: cancellationRules
  type: array
- description: list of payment methods, allowed by provider
  name: methodsOfPaymentAccepted
  type: array
- description: list of discount codes
  name: discountCodes
  type: array
- description: ''
  name: distance
  type: object
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
schema_file: json-schema/transfer-booking-transfer-schema.json
slug: transfer-booking-transfer
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
title: Transfer
---
